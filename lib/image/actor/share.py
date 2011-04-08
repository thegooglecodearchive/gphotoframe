from gettext import gettext as _

from ...utils.iconimage import IconImage
from ...plugins.tumblr import TumblrShare
from trash import ActorTrashIcon, TrashDialog

class ActorShareIcon(ActorTrashIcon):

    def _set_dialog(self):
        self.dialog = ShareDialog()

    def _check_photo(self):
        return self.photo.can_share()

    def _get_icon(self):
        return IconImage('emblem-shared')

    def _get_ui_data(self):
        self._set_ui_options('share', False, 0)

    def _enter_cb(self, w, e, tooltip):
        tooltip.update_text(_("Share on Tumblr"))

class ShareDialog(TrashDialog):

    def _set_variable(self, photo):
        self.text = [ _("Share this photo on Tumblr?"),
                      _("This photo will be shared on Tumblr.") ]
        share = TumblrShare()
        self.delete_method = share.add
