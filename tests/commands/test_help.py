import unittest
import sublime
from unittest.mock import MagicMock, patch

from Javatar.commands.javatar_help import JavatarHelpCommand

expected_output = r'''## Javatar Report
### System Informations
* Javatar Version: `1.0`
* Sublime Version: `0`
* Package Path: ``
* Javatar Channel: `production`
* Sublime Channel: `3dev`
* Is Debug Mode: `False`
* Platform: `win32`
* As Packages: `False`
* Package Control: `False`
* Architecture: `64bit`
* Javatar's Parent Folder: `javatar`
* Is Project: `False`
* Is File: `False`
* Is Java: `True`

### Action List
1. Clicked on blah blah
2. Typed in blargy blah
'''


class TestHelp(unittest.TestCase):
    @patch('Javatar.commands.javatar_help.get_settings')
    @patch('Javatar.commands.javatar_help.JavatarHelpCommand.get_actions')
    @patch('Javatar.commands.javatar_help.is_java')
    @patch('Javatar.commands.javatar_help.is_file')
    @patch('Javatar.commands.javatar_help.is_project')
    @patch('Javatar.commands.javatar_help.get_version', return_value='1.0')
    @patch('Javatar.commands.javatar_help.get_javatar_parent', return_value='javatar')
    @patch('sublime.packages_path', return_value='')
    @patch('sublime.installed_packages_path', return_value='')
    @patch('sublime_api.architecture', return_value='64bit')
    @patch('sublime_api.platform', return_value='win32')
    @patch('sublime_api.channel', return_value='3dev')
    @patch('sublime_api.version', return_value='0')
    def test_run_help(self, version, channel, platform, architecture, installed_packages_path, packages_path, get_javatar_parent,
                      get_version, is_project, is_file, is_java, get_actions, get_settings):
        is_project.return_value = False
        is_file.return_value = False
        is_java.return_value = True
        get_settings.side_effect = {
            'enable_actions_history': True,
            'package_channel': 'production',
            'debug_mode': False
        }.get
        get_actions.return_value = [
            'Clicked on blah blah',
            'Typed in blargy blah'
        ]

        window = MagicMock(spec=sublime.Window)
        inst = JavatarHelpCommand(window)

        inst.run(selector="Blarg", action="actions_history")

        window.new_file.assert_was_called()
        view = window.new_file.return_value
        view.set_scratch.assert_was_called()
        view.set_name.assert_was_called_with('Javatar Actions History Report')
        view.run_command.assert_was_called(
            "javatar_utils", {'util_type': 'set_read_only'}
        )
        text = view.run_command.call_args_list[0][0][1]['text']

        self.assertEqual(
            expected_output,
            text
        )

    @patch('Javatar.commands.javatar_help.get_action')
    def test_get_actions(self, get_action):
        window = MagicMock(spec=sublime.Window)
        inst = JavatarHelpCommand(window)

        inst.get_actions('One|Two')

        get_action.return_value.get_action.assert_called_with(
            ['One'], ['Two']
        )
