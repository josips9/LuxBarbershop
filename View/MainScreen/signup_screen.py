from View.base_screen import BaseScreenView


class SignUpScreenView(BaseScreenView):
    def model_is_changed(self, success: bool = True, error: str = "") -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.

        :param success:
            Optional argument indicating the success status. Default is True.
        :param error:
            Optional argument providing an error message. Default is an empty string.

        """
        if success:
            pass
        else:
            pass
