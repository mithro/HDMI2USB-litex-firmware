import sys

import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject


from ck_ab import ck_ab

class ck_video(ck_ab):

    def run_pipeline(self, pipeline):

        if self.args.verbose: print(pipeline)

        def on_eos(bus, message):
            print('Received EOS-Signal')
            sys.exit(0)

        def on_error(bus, message):
            print('Received Error-Signal')
            (error, debug) = message.parse_error()
            print('Error-Details: #%u: %s' % (error.code, debug))
            sys.exit(2)

        Gst.init([])

        print('starting pipeline...')
        senderPipeline = Gst.parse_launch(pipeline)

        # Binding End-of-Stream-Signal on Source-Pipeline
        senderPipeline.bus.add_signal_watch()
        senderPipeline.bus.connect("message::eos", on_eos)
        senderPipeline.bus.connect("message::error", on_error)

        print("playing...")
        senderPipeline.set_state(Gst.State.PLAYING)

        mainloop = GObject.MainLoop()
        try:
            mainloop.run()
        except KeyboardInterrupt:
            print('Terminated via Ctrl-C')

        print('Shutting down...')
        senderPipeline.set_state(Gst.State.NULL)
        print('Done.')

        return

    def test(self):
        pipeline = "v4l2src device={dev} num-buffers=3 ! jpegdec ! fakesink".format(dev=self.args.video)
        self.run_pipeline(pipeline)


if __name__=='__main__':
    t = ck_video()
    t.main()


"""
# gst-launch-1.0 v4l2src num-buffers=3 ! jpegdec ! fakesink

good:
Setting pipeline to PAUSED ...
Pipeline is live and does not need PREROLL ...
Setting pipeline to PLAYING ...
New clock: GstSystemClock
Got EOS from element "pipeline0".
Execution ended after 0:00:00.140227228
Setting pipeline to PAUSED ...
Setting pipeline to READY ...
Setting pipeline to NULL ...
Freeing pipeline ...

bad:
Setting pipeline to PAUSED ...
Pipeline is live and does not need PREROLL ...
Setting pipeline to PLAYING ...
New clock: GstSystemClock
ERROR: from element /GstPipeline:pipeline0/GstJpegDec:jpegdec0: Failed to decode JPEG image
Additional debug info:
gstjpegdec.c(1194): gst_jpeg_dec_handle_frame (): /GstPipeline:pipeline0/GstJpegDec:jpegdec0:
Decode error #62: Invalid JPEG file structure: SOS before SOF
Execution ended after 0:00:00.495845910
Setting pipeline to PAUSED ...
Setting pipeline to READY ...
Setting pipeline to NULL ...
Freeing pipeline ...

"""
