## Javatar
A Sublime Text 3 Plugin for Java Development

JavatarDoc: [https://javatar.readthedocs.org/](https://javatar.readthedocs.org/)<br \>
Report Issue: [https://github.com/spywhere/Javatar/issues](https://github.com/spywhere/Javatar/issues)

[![Gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/spywhere/Javatar?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)|[![Issues](https://img.shields.io/github/issues/spywhere/Javatar.svg?style=flat)](https://github.com/spywhere/Javatar/issues)|[![Release](https://img.shields.io/github/release/spywhere/Javatar.svg?style=flat)](https://github.com/spywhere/Javatar/releases)
:---:|:---:|:---:
[![Build Status](https://img.shields.io/travis/spywhere/Javatar/release.svg?style=flat)](https://travis-ci.org/spywhere/Javatar)|[![Build Status](https://img.shields.io/travis/spywhere/Javatar/master.svg?style=flat)](https://travis-ci.org/spywhere/Javatar)|[![License](http://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat)](https://github.com/spywhere/Javatar/blob/master/LICENSE)
release|master (develop)

## Javatar v2.0.0-prebeta.3
To install a prerelease version, please add `Javatar` to the `install_preleases` list in the Package Control user's settings.

Prerelease version contains a new feature which will introduce in Javatar v2.0.0 but please keep in mind that prerelease version is not a stable build to use and not all features are fully working.

Please note that Javatar v1.0.0 settings **are not compatible** with Javatar v2.0.0 settings. Even though some settings remain the same.

#### What's new in Javatar v2.0.0-prebeta.3
- Remove in v2.0.0
  - Package Channel
  - Javatar Calls
  - Correct Class (use Organize Imports instead)
  - **Packages Manager (now switched to a new searching system)**
- Build System
  - Java library path supports
  - Multiple builder supports
  - Multiple source folders supports
  - Run main class without open the main class
  - Incremental builds (build only changed files)
- Dependency Management
  - Maven dependency supports (download from the central repository)
  - **Java packages now search using actual files rather than Javatar packages**
- Linter supported
  - Java linter supported via SublimeLinter
- Status Management
  - More cleaner ways to show a status message with various contexts
- Console
  - A cleaner ways to indicate multiple instance of programs
  - EOF signal supported (by clearing the console)
- Macro
  - Complex macros supports
- Plugin System
  - Plugin API (to extends the Javatar functionalities)
- Miscellaneous
  - Reduce memory usage
  - Missing project settings detection

\* *Bold texts are changes from the previous release*