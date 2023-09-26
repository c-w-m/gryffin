# Failed Development Installation

```shell
gryffin [ master][!?][🐍 v3.10.11(.gryffin_dev310)]
❯ pip install -e .
Looking in indexes: https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/simple
Obtaining file:///C:/code/ghcwm/gryffin
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Preparing editable metadata (pyproject.toml) ... done
Collecting torch
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/8a/e7/c216fe520b877cf4fe03858c825cd2031ca3e81e455b89639c9b5ec91981/torch-2.0.1-cp310-cp310-win_amd64.whl (172.3 MB)
Collecting pandas
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/ce/cd/a7c2cbffe2afff975349e60b14b63a448162145a7acac8ba12ddc2ed78a8/pandas-2.1.1-cp310-cp310-win_amd64.whl (10.7 MB)
Collecting deap
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/38/6c/e240099dc857d38ec9e0eca7c020c3e18274a873e0f2ac3004e3b8783156/deap-1.4.1-cp310-cp310-win_amd64.whl (109 kB)
Collecting sqlalchemy
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/31/f6/3a2ccb16aae346eccc11836ac7188be1da12591bf19834826ae63b051f23/SQLAlchemy-2.0.21-cp310-cp310-win_amd64.whl (2.0 MB)
Collecting rich
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/c1/d1/23ba6235ed82883bb416f57179d1db2c05f3fb8e5d83c18660f9ab6f09c9/rich-13.5.3-py3-none-any.whl (239 kB)
Collecting matter-chimera
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/19/94/5f9ed864987833065cd50db8ad78471d496fef5266fea72289a2afbc480c/matter_chimera-1.0-py3-none-any.whl (7.2 kB)
Collecting numpy
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/cc/05/ef9fc04adda45d537619ea956bc33489f50a46badc949c4280d8309185ec/numpy-1.26.0-cp310-cp310-win_amd64.whl (15.8 MB)
Collecting torchbnn
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/68/47/4629eb37ec9e28d162f76cc44a988bb1f29c7fb2598918b29a06e342fa0d/torchbnn-1.2-py3-none-any.whl (12 kB)
Collecting python-dateutil>=2.8.2
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/36/7a/87837f39d0296e723bb9b62bbb257d0355c7f6128853c78955f57342a56d/python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
Collecting pytz>=2020.1
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/32/4d/aaf7eff5deb402fd9a24a1449a8119f00d74ae9c2efa79f8ef9994261fc2/pytz-2023.3.post1-py2.py3-none-any.whl (502 kB)
Collecting tzdata>=2022.1
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/d5/fb/a79efcab32b8a1f1ddca7f35109a50e4a80d42ac1c9187ab46522b2407d7/tzdata-2023.3-py2.py3-none-any.whl (341 kB)
Collecting markdown-it-py>=2.2.0
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/42/d7/1ec15b46af6af88f19b8e5ffea08fa375d433c998b8a7639e76935c14f1f/markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
Collecting pygments<3.0.0,>=2.13.0
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/43/88/29adf0b44ba6ac85045e63734ae0997d3c58d8b1a91c914d240828d0d73d/Pygments-2.16.1-py3-none-any.whl (1.2 MB)
Collecting typing-extensions>=4.2.0
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/24/21/7d397a4b7934ff4028987914ac1044d3b7d52712f30e2ac7a2ae5bc86dd0/typing_extensions-4.8.0-py3-none-any.whl (31 kB)
Collecting greenlet!=0.4.17
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/53/0f/637f6e18e1980ebd2eedd8a9918a7898a6fe44f6188f6f39c6d9181c9891/greenlet-2.0.2-cp310-cp310-win_amd64.whl (192 kB)
Collecting filelock
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/5e/5d/97afbafd9d584ff1b45fcb354a479a3609bd97f912f8f1f6c563cb1fae21/filelock-3.12.4-py3-none-any.whl (11 kB)
Collecting jinja2
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/bc/c3/f068337a370801f372f2f8f6bad74a5c140f6fda3d9de154052708dd3c65/Jinja2-3.1.2-py3-none-any.whl (133 kB)
Collecting networkx
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/a8/05/9d4f9b78ead6b2661d6e8ea772e111fc4a9fbd866ad0c81906c11206b55e/networkx-3.1-py3-none-any.whl (2.1 MB)
Collecting sympy
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/d2/05/e6600db80270777c4a64238a98d442f0fd07cc8915be2a1c16da7f2b9e74/sympy-1.12-py3-none-any.whl (5.7 MB)
Collecting mdurl~=0.1
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/b3/38/89ba8ad64ae25be8de66a6d463314cf1eb366222074cfda9ee839c56a4b4/mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Collecting six>=1.5
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/d9/5a/e7c31adbe875f2abbb91bd84cf2dc52d792b5a01506781dbcf25c91daf11/six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting MarkupSafe>=2.0
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/84/a8/c4aebb8a14a1d39d5135eb8233a0b95831cdc42c4088358449c3ed657044/MarkupSafe-2.1.3-cp310-cp310-win_amd64.whl (17 kB)
Collecting mpmath>=0.19
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/43/e3/7d92a15f894aa0c9c4b49b8ee9ac9850d6e63b03c9c32c0367a13ae62209/mpmath-1.3.0-py3-none-any.whl (536 kB)
Building wheels for collected packages: gryffin
  Building editable for gryffin (pyproject.toml) ... error
  error: subprocess-exited-with-error

  × Building editable for gryffin (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [245 lines of output]
      running editable_wheel
      creating C:\Users\craigmiller\AppData\Local\Temp\pip-wheel-kjoo3aax\.tmp-9s4f5zx9\gryffin.egg-info
      writing C:\Users\craigmiller\AppData\Local\Temp\pip-wheel-kjoo3aax\.tmp-9s4f5zx9\gryffin.egg-info\PKG-INFO
      writing dependency_links to C:\Users\craigmiller\AppData\Local\Temp\pip-wheel-kjoo3aax\.tmp-9s4f5zx9\gryffin.egg-info\dependency_links.txt
      writing entry points to C:\Users\craigmiller\AppData\Local\Temp\pip-wheel-kjoo3aax\.tmp-9s4f5zx9\gryffin.egg-info\entry_points.txt
      writing requirements to C:\Users\craigmiller\AppData\Local\Temp\pip-wheel-kjoo3aax\.tmp-9s4f5zx9\gryffin.egg-info\requires.txt
      writing top-level names to C:\Users\craigmiller\AppData\Local\Temp\pip-wheel-kjoo3aax\.tmp-9s4f5zx9\gryffin.egg-info\top_level.txt
      writing manifest file 'C:\Users\craigmiller\AppData\Local\Temp\pip-wheel-kjoo3aax\.tmp-9s4f5zx9\gryffin.egg-info\SOURCES.txt'
      reading manifest file 'C:\Users\craigmiller\AppData\Local\Temp\pip-wheel-kjoo3aax\.tmp-9s4f5zx9\gryffin.egg-info\SOURCES.txt'
      reading manifest template 'MANIFEST.in'
      warning: no files found matching 'requirements.txt'
      adding license file 'LICENSE.md'
      writing manifest file 'C:\Users\craigmiller\AppData\Local\Temp\pip-wheel-kjoo3aax\.tmp-9s4f5zx9\gryffin.egg-info\SOURCES.txt'
      creating 'C:\Users\craigmiller\AppData\Local\Temp\pip-wheel-kjoo3aax\.tmp-9s4f5zx9\gryffin-0+untagged.325.g8696bf8.dirty.dist-info'
      C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\wheel\bdist_wheel.py:109: RuntimeWarning: Config variable 'Py_DEBUG' is unset, Python ABI tag may be incorrect
        if get_flag("Py_DEBUG", hasattr(sys, "gettotalrefcount"), warn=(impl == "cp")):
      creating C:\Users\craigmiller\AppData\Local\Temp\pip-wheel-kjoo3aax\.tmp-9s4f5zx9\gryffin-0+untagged.325.g8696bf8.dirty.dist-info\WHEEL
      running build_py
      C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\command\editable_wheel.py:293: SetuptoolsDeprecationWarning: Customization incompatible with editable install
      !!

              ********************************************************************************
                              Traceback (most recent call last):
                File "C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\command\editable_wheel.py", line 299, in _safely_run
                  return self.run_command(cmd_name)
                File "C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\_distutils\cmd.py", line 318, in run_command
                  self.distribution.run_command(command)
                File "C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\dist.py", line 989, in run_command
                  super().run_command(command)
                File "C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\_distutils\dist.py", line 988, in run_command
                  cmd_obj.run()
                File "C:\code\ghcwm\gryffin\versioneer.py", line 1559, in run
                  write_to_version_file(target_versionfile, versions)
                File "C:\code\ghcwm\gryffin\versioneer.py", line 1220, in write_to_version_file
                  os.unlink(filename)
              FileNotFoundError: [WinError 3] The system cannot find the path specified: 'C:\\Users\\CRAIGM~1\\AppData\\Local\\Temp\\tmp2hgrc10b.build-lib\\gryffin/_version.py'


                              If you are seeing this warning it is very likely that a setuptools
                              plugin or customization overrides the `build_py` command, without
                              taking into consideration how editable installs run build steps
                              starting from setuptools v64.0.0.

                              Plugin authors and developers relying on custom build steps are
                              encouraged to update their `build_py` implementation considering the
                              information about editable installs in
                              https://setuptools.pypa.io/en/latest/userguide/extension.html.

                              For the time being `setuptools` will silence this error and ignore
                              the faulty command, but this behaviour will change in future versions.

              ********************************************************************************

      !!
        self._safely_run(name)
      UPDATING C:\Users\CRAIGM~1\AppData\Local\Temp\tmp2hgrc10b.build-lib\gryffin/_version.py
      running build_ext
      building 'gryffin.bayesian_network.kernel_evaluations' extension
      creating C:\Users\CRAIGM~1\AppData\Local\Temp\tmprtexq7ny.build-temp\Release
      creating C:\Users\CRAIGM~1\AppData\Local\Temp\tmprtexq7ny.build-temp\Release\src
      creating C:\Users\CRAIGM~1\AppData\Local\Temp\tmprtexq7ny.build-temp\Release\src\gryffin
      creating C:\Users\CRAIGM~1\AppData\Local\Temp\tmprtexq7ny.build-temp\Release\src\gryffin\bayesian_network
      "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.36.32532\bin\HostX86\x64\cl.exe" /c /nologo /O2 /W3 /GL /DNDEBUG /MD -IC:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\numpy\core\include -IC:\code\ghcwm\gryffin\.gryffin_dev310\include -IC:\Users\craigmiller\scoop\apps\python310\current\include -IC:\Users\craigmiller\scoop\apps\python310\current\Include "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.36.32532\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Tools\MSVC\14.36.32532\ATLMFC\include" "-IC:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\VS\include" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.22000.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22000.0\\um" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22000.0\\shared" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22000.0\\winrt" "-IC:\Program Files (x86)\Windows Kits\10\\include\10.0.22000.0\\cppwinrt" "-IC:\Program Files (x86)\Windows Kits\NETFXSDK\4.8\include\um" -IC:\bin\Graphviz\include /Tcsrc/gryffin/bayesian_network/kernel_evaluations.c /FoC:\Users\CRAIGM~1\AppData\Local\Temp\tmprtexq7ny.build-temp\Release\src/gryffin/bayesian_network/kernel_evaluations.obj
      kernel_evaluations.c
      C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\numpy\core\include\numpy\npy_1_7_deprecated_api.h(14) : Warning Msg: Using deprecated NumPy API, disable it with #define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
      src/gryffin/bayesian_network/kernel_evaluations.c(1595): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(1601): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(2831): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(2906): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(2931): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(3043): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(3212): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(3487): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(3544): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(4092): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(4134): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(4366): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(4401): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(4416): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(4458): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(4677): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(4712): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(4727): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(4770): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(5194): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(5229): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(5244): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(5283): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(5566): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(5660): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(5675): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(5714): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(5995): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(6089): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(6104): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(6150): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(6460): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(6494): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(6522): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(6626): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(6791): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(6822): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(7076): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(7133): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(7846): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(7878): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(7949): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(7970): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(8001): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(8023): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(8054): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(8076): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(8107): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(8129): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(8160): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(8182): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(8213): error C2039: 'use_tracing': is not a member of '_ts'
      C:\Users\craigmiller\scoop\apps\python310\current\include\cpython/pystate.h(60): note: see declaration of '_ts'
      src/gryffin/bayesian_network/kernel_evaluations.c(8213): fatal error C1003: error count exceeds 100; stopping compilation
      Traceback (most recent call last):
        File "C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\_distutils\_msvccompiler.py", line 419, in compile
          self.spawn(args)
        File "C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\_distutils\_msvccompiler.py", line 517, in spawn
          return super().spawn(cmd, env=env)
        File "C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\_distutils\ccompiler.py", line 1041, in spawn
          spawn(cmd, dry_run=self.dry_run, **kwargs)
        File "C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\_distutils\spawn.py", line 70, in spawn
          raise DistutilsExecError(
      distutils.errors.DistutilsExecError: command 'C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.36.32532\\bin\\HostX86\\x64\\cl.exe' failed with exit code 2

      During handling of the above exception, another exception occurred:

      Traceback (most recent call last):
        File "C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\command\editable_wheel.py", line 156, in run
          self._create_wheel_file(bdist_wheel)
        File "C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\command\editable_wheel.py", line 345, in _create_wheel_file
          files, mapping = self._run_build_commands(dist_name, unpacked, lib, tmp)
        File "C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\command\editable_wheel.py", line 268, in _run_build_commands
          self._run_build_subcommands()
        File "C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\command\editable_wheel.py", line 295, in _run_build_subcommands
          self.run_command(name)
        File "C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\_distutils\cmd.py", line 318, in run_command
          self.distribution.run_command(command)
        File "C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\dist.py", line 989, in run_command
          super().run_command(command)
        File "C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\_distutils\dist.py", line 988, in run_command
          cmd_obj.run()
        File "C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\command\build_ext.py", line 88, in run
          _build_ext.run(self)
        File "C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\_distutils\command\build_ext.py", line 345, in run
          self.build_extensions()
        File "C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\_distutils\command\build_ext.py", line 467, in build_extensions
          self._build_extensions_serial()
        File "C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\_distutils\command\build_ext.py", line 493, in _build_extensions_serial
          self.build_extension(ext)
        File "C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\command\build_ext.py", line 249, in build_extension
          _build_ext.build_extension(self, ext)
        File "C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\Cython\Distutils\build_ext.py", line 127, in build_extension
          super(build_ext, self).build_extension(ext)
        File "C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\_distutils\command\build_ext.py", line 548, in build_extension
          objects = self.compiler.compile(
        File "C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\_distutils\_msvccompiler.py", line 421, in compile
          raise CompileError(msg)
      distutils.errors.CompileError: command 'C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.36.32532\\bin\\HostX86\\x64\\cl.exe' failed with exit code 2
      C:\Users\craigmiller\AppData\Local\Temp\pip-build-env-i6np6nsk\overlay\Lib\site-packages\setuptools\_distutils\dist.py:988: _DebuggingTips: Problem in editable installation.
      !!

              ********************************************************************************
              An error happened while installing `gryffin` in editable mode.

              The following steps are recommended to help debug this problem:

              - Try to install the project normally, without using the editable mode.
                Does the error still persist?
                (If it does, try fixing the problem before attempting the editable mode).
              - If you are using binary extensions, make sure you have all OS-level
                dependencies installed (e.g. compilers, toolchains, binary libraries, ...).
              - Try the latest version of setuptools (maybe the error was already fixed).
              - If you (or your project dependencies) are using any setuptools extension
                or customization, make sure they support the editable mode.

              After following the steps above, if the problem still persists and
              you think this is related to how setuptools handles editable installations,
              please submit a reproducible example
              (see https://stackoverflow.com/help/minimal-reproducible-example) to:

                  https://github.com/pypa/setuptools/issues

              See https://setuptools.pypa.io/en/latest/userguide/development_mode.html for details.
              ********************************************************************************

      !!
        cmd_obj.run()
      error: command 'C:\\Program Files\\Microsoft Visual Studio\\2022\\Community\\VC\\Tools\\MSVC\\14.36.32532\\bin\\HostX86\\x64\\cl.exe' failed with exit code 2
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building editable for gryffin
Failed to build gryffin
ERROR: Could not build wheels for gryffin, which is required to install pyproject.toml-based projects

[notice] A new release of pip is available: 23.0.1 -> 23.2.1
[notice] To update, run: python.exe -m pip install --upgrade pip

gryffin [ master][!?][🐍 v3.10.11(.gryffin_dev310)][⏱ 3m24s]
❯

```

---
