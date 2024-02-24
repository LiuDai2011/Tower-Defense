class Content:
    _launcher = None
    _set_launcher = False

    @staticmethod
    def get_launcher():
        return Content._launcher

    @staticmethod
    def set_launcher(launcher):
        assert not Content._set_launcher
        Content._launcher = launcher
        Content._set_launcher = True
        return Content

    @staticmethod
    def launch():
        Content._launcher.launch()
