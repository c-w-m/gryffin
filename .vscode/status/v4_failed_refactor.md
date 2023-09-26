# Failed Refactor Installation

## FIXME -> v4 refactor of `kernel_prob_reshaping.c`

```shell
  src/gryffin/bayesian_network/kernel_prob_reshaping.c(3083): warning C4244: '=': conversion from 'npy_intp' to 'int', possible loss of data
      src/gryffin/bayesian_network/kernel_prob_reshaping.c(3092): warning C4244: '=': conversion from 'npy_intp' to 'int', possible loss of data
      src/gryffin/bayesian_network/kernel_prob_reshaping.c(3101): warning C4244: '=': conversion from 'npy_intp' to 'int', possible loss of data
      src/gryffin/bayesian_network/kernel_prob_reshaping.c(3110): warning C4244: '=': conversion from 'npy_intp' to 'int', possible loss of data

# FIXME-1
      src/gryffin/bayesian_network/kernel_prob_reshaping.c(19571): error C2105: '++' needs l-value
      src/gryffin/bayesian_network/kernel_prob_reshaping.c(19573): error C2105: '--' needs l-value
      
# FIXME-2
      src/gryffin/bayesian_network/kernel_prob_reshaping.c(19882): error C2105: '++' needs l-value
      src/gryffin/bayesian_network/kernel_prob_reshaping.c(19884): error C2105: '--' needs l-value

# FIXME-3
      src/gryffin/bayesian_network/kernel_prob_reshaping.c(20132): error C2105: '++' needs l-value
      src/gryffin/bayesian_network/kernel_prob_reshaping.c(20134): error C2105: '--' needs l-value

      src/gryffin/bayesian_network/kernel_prob_reshaping.c(20785): warning C4996: 'PyEval_InitThreads': deprecated in 3.9
      src/gryffin/bayesian_network/kernel_prob_reshaping.c(22017): warning C4996: '_PyUnicode_get_wstr_length': deprecated in 3.3
      src/gryffin/bayesian_network/kernel_prob_reshaping.c(22033): warning C4996: '_PyUnicode_get_wstr_length': deprecated in 3.3
      src/gryffin/bayesian_network/kernel_prob_reshaping.c(22893): warning C4996: 'PyUnicode_FromUnicode': deprecated in 3.3
```

---

## Refactor Code

### FIXME-1

```c
    Py_SET_REFCNT(o, Py_REFCNT(o) + 1);  //FIXME-1: ++Py_REFCNT(o);
    __pyx_array___dealloc__(o);
    Py_SET_REFCNT(o, Py_REFCNT(o) - 1);  //FIXME-1: --Py_REFCNT(o);
```

![kernel_prob_reshaping(19571)-v4_fix1.png](v4_refactor/img/kernel_prob_reshaping(19571)-v4_fix1.png)

### FIXME-2

```c
    Py_SET_REFCNT(o, Py_REFCNT(o) + 1);  //FIXME-2: ++Py_REFCNT(o);
    __pyx_memoryview___dealloc__(o);
    Py_SET_REFCNT(o, Py_REFCNT(o) - 1);  //FIXME-2: --Py_REFCNT(o);
```

![kernel_prob_reshaping(19571)-v4_fix2.png](v4_refactor/img/kernel_prob_reshaping(19571)-v4_fix2.png)

### FIXME-3

```c
    Py_SET_REFCNT(o, Py_REFCNT(o) + 1);  //FIXME--3 ++Py_REFCNT(o);
    __pyx_memoryviewslice___dealloc__(o);
    Py_SET_REFCNT(o, Py_REFCNT(o) - 1);  //FIXME-2: --Py_REFCNT(o);
```

![kernel_prob_reshaping(19571)-v4_fix3.png](v4_refactor/img/kernel_prob_reshaping(19571)-v4_fix3.png)

## Successfully Installed With Pip Error Message

```shell
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
oldest-supported-numpy 2023.8.3 requires numpy==1.21.6; python_version == "3.10" and platform_machine != "loongarch64", but you have numpy 1.26.0 which is incompatible.
```

<details>

```shell
gryffin [ master][!?][🐍 v3.10.11(.gryffin_dev310)]
❯ pip install -e .
Looking in indexes: https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/simple
Obtaining file:///C:/code/ghcwm/gryffin
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Preparing editable metadata (pyproject.toml) ... done
Requirement already satisfied: numpy in c:\code\ghcwm\gryffin\.gryffin_dev310\lib\site-packages (from gryffin==0+untagged.325.g8696bf8.dirty) (1.21.6)
Collecting sqlalchemy (from gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/31/f6/3a2ccb16aae346eccc11836ac7188be1da12591bf19834826ae63b051f23/SQLAlchemy-2.0.21-cp310-cp310-win_amd64.whl (2.0 MB)
Collecting rich (from gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/c1/d1/23ba6235ed82883bb416f57179d1db2c05f3fb8e5d83c18660f9ab6f09c9/rich-13.5.3-py3-none-any.whl (239 kB)
Collecting pandas (from gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/ce/cd/a7c2cbffe2afff975349e60b14b63a448162145a7acac8ba12ddc2ed78a8/pandas-2.1.1-cp310-cp310-win_amd64.whl (10.7 MB)
Collecting matter-chimera (from gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/19/94/5f9ed864987833065cd50db8ad78471d496fef5266fea72289a2afbc480c/matter_chimera-1.0-py3-none-any.whl (7.2 kB)
Collecting deap (from gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/38/6c/e240099dc857d38ec9e0eca7c020c3e18274a873e0f2ac3004e3b8783156/deap-1.4.1-cp310-cp310-win_amd64.whl (109 kB)
Collecting torch (from gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/8a/e7/c216fe520b877cf4fe03858c825cd2031ca3e81e455b89639c9b5ec91981/torch-2.0.1-cp310-cp310-win_amd64.whl (172.3 MB)
Collecting torchbnn (from gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/68/47/4629eb37ec9e28d162f76cc44a988bb1f29c7fb2598918b29a06e342fa0d/torchbnn-1.2-py3-none-any.whl (12 kB)
Collecting numpy (from gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/cc/05/ef9fc04adda45d537619ea956bc33489f50a46badc949c4280d8309185ec/numpy-1.26.0-cp310-cp310-win_amd64.whl (15.8 MB)
Collecting python-dateutil>=2.8.2 (from pandas->gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/36/7a/87837f39d0296e723bb9b62bbb257d0355c7f6128853c78955f57342a56d/python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
Collecting pytz>=2020.1 (from pandas->gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/32/4d/aaf7eff5deb402fd9a24a1449a8119f00d74ae9c2efa79f8ef9994261fc2/pytz-2023.3.post1-py2.py3-none-any.whl (502 kB)
Collecting tzdata>=2022.1 (from pandas->gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/d5/fb/a79efcab32b8a1f1ddca7f35109a50e4a80d42ac1c9187ab46522b2407d7/tzdata-2023.3-py2.py3-none-any.whl (341 kB)
Collecting markdown-it-py>=2.2.0 (from rich->gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/42/d7/1ec15b46af6af88f19b8e5ffea08fa375d433c998b8a7639e76935c14f1f/markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
Collecting pygments<3.0.0,>=2.13.0 (from rich->gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/43/88/29adf0b44ba6ac85045e63734ae0997d3c58d8b1a91c914d240828d0d73d/Pygments-2.16.1-py3-none-any.whl (1.2 MB)
Collecting typing-extensions>=4.2.0 (from sqlalchemy->gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/24/21/7d397a4b7934ff4028987914ac1044d3b7d52712f30e2ac7a2ae5bc86dd0/typing_extensions-4.8.0-py3-none-any.whl (31 kB)
Collecting greenlet!=0.4.17 (from sqlalchemy->gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/53/0f/637f6e18e1980ebd2eedd8a9918a7898a6fe44f6188f6f39c6d9181c9891/greenlet-2.0.2-cp310-cp310-win_amd64.whl (192 kB)
Collecting filelock (from torch->gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/5e/5d/97afbafd9d584ff1b45fcb354a479a3609bd97f912f8f1f6c563cb1fae21/filelock-3.12.4-py3-none-any.whl (11 kB)
Collecting sympy (from torch->gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/d2/05/e6600db80270777c4a64238a98d442f0fd07cc8915be2a1c16da7f2b9e74/sympy-1.12-py3-none-any.whl (5.7 MB)
Collecting networkx (from torch->gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/a8/05/9d4f9b78ead6b2661d6e8ea772e111fc4a9fbd866ad0c81906c11206b55e/networkx-3.1-py3-none-any.whl (2.1 MB)
Collecting jinja2 (from torch->gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/bc/c3/f068337a370801f372f2f8f6bad74a5c140f6fda3d9de154052708dd3c65/Jinja2-3.1.2-py3-none-any.whl (133 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich->gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/b3/38/89ba8ad64ae25be8de66a6d463314cf1eb366222074cfda9ee839c56a4b4/mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Collecting six>=1.5 (from python-dateutil>=2.8.2->pandas->gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/d9/5a/e7c31adbe875f2abbb91bd84cf2dc52d792b5a01506781dbcf25c91daf11/six-1.16.0-py2.py3-none-any.whl (11 kB)
Collecting MarkupSafe>=2.0 (from jinja2->torch->gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/84/a8/c4aebb8a14a1d39d5135eb8233a0b95831cdc42c4088358449c3ed657044/MarkupSafe-2.1.3-cp310-cp310-win_amd64.whl (17 kB)
Collecting mpmath>=0.19 (from sympy->torch->gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/43/e3/7d92a15f894aa0c9c4b49b8ee9ac9850d6e63b03c9c32c0367a13ae62209/mpmath-1.3.0-py3-none-any.whl (536 kB)
Building wheels for collected packages: gryffin
  Building editable for gryffin (pyproject.toml) ... done
  Created wheel for gryffin: filename=gryffin-0+untagged.325.g8696bf8.dirty-0.editable-cp310-cp310-win_amd64.whl size=7946 sha256=c597c524d4a79a799bc218d6dd2c80b9d257c90d1861b636b659fb52e7f90186
  Stored in directory: C:\Users\craigmiller\AppData\Local\Temp\pip-ephem-wheel-cache-v6wtlko8\wheels\e3\e7\a8\bad0faefb603dcc7c3c5d75c3af158a50199aa8b2ea6c64c3a
Successfully built gryffin
Installing collected packages: pytz, mpmath, tzdata, typing-extensions, torchbnn, sympy, six, pygments, numpy, networkx, mdurl, MarkupSafe, greenlet, filelock, sqlalchemy, python-dateutil, matter-chimera, markdown-it-py, jinja2, deap, torch, rich, pandas, gryffin
  Attempting uninstall: numpy
    Found existing installation: numpy 1.21.6
    Uninstalling numpy-1.21.6:
      Successfully uninstalled numpy-1.21.6
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
oldest-supported-numpy 2023.8.3 requires numpy==1.21.6; python_version == "3.10" and platform_machine != "loongarch64", but you have numpy 1.26.0 which is incompatible.
Successfully installed MarkupSafe-2.1.3 deap-1.4.1 filelock-3.12.4 greenlet-2.0.2 gryffin-0+untagged.325.g8696bf8.dirty jinja2-3.1.2 markdown-it-py-3.0.0 matter-chimera-1.0 mdurl-0.1.2 mpmath-1.3.0 networkx-3.1 numpy-1.26.0 pandas-2.1.1 pygments-2.16.1 python-dateutil-2.8.2 pytz-2023.3.post1 rich-13.5.3 six-1.16.0 sqlalchemy-2.0.21 sympy-1.12 torch-2.0.1 torchbnn-1.2 typing-extensions-4.8.0 tzdata-2023.3

gryffin [ master][!?][🐍 v3.10.11(.gryffin_dev310)][⏱ 21m3s]
```

</details>

---

## Test

### `resource` error

<details>

```shell
gryffin\tests [ master][!?][🐍 v3.10.11(.gryffin_dev310)][⏱ 24s]
❯ pytest  
==================================================================================================================== test session starts =====================================================================================================================
platform win32 -- Python 3.10.11, pytest-7.4.2, pluggy-1.3.0
rootdir: C:\code\ghcwm\gryffin
collected 0 items / 5 errors

=========================================================================================================================== ERRORS ===========================================================================================================================
_________________________________________________________________________________________________________ ERROR collecting tests/test_categorical.py _________________________________________________________________________________________________________ 
ImportError while importing test module 'C:\code\ghcwm\gryffin\tests\test_categorical.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\craigmiller\scoop\apps\python310\current\lib\importlib\__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
test_categorical.py:5: in <module>
    from gryffin import Gryffin
..\src\gryffin\__init__.py:3: in <module>
    from .gryffin import Gryffin
..\src\gryffin\gryffin.py:5: in <module>
    from .acquisition import Acquisition
..\src\gryffin\acquisition\__init__.py:3: in <module>
    from .acquisition import Acquisition
..\src\gryffin\acquisition\acquisition.py:11: in <module>
    from .gradient_optimizer import GradientOptimizer
..\src\gryffin\acquisition\gradient_optimizer\__init__.py:6: in <module>
    from .gradient_optimizer import GradientOptimizer
..\src\gryffin\acquisition\gradient_optimizer\gradient_optimizer.py:7: in <module>
    from gryffin.utilities import Logger
..\src\gryffin\utilities\__init__.py:24: in <module>
    from .infos import parse_time, memory_usage, print_memory_usage
..\src\gryffin\utilities\infos.py:3: in <module>
    import resource
E   ModuleNotFoundError: No module named 'resource'
_________________________________________________________________________________________________________ ERROR collecting tests/test_constraints.py _________________________________________________________________________________________________________ 
ImportError while importing test module 'C:\code\ghcwm\gryffin\tests\test_constraints.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\craigmiller\scoop\apps\python310\current\lib\importlib\__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
test_constraints.py:5: in <module>
    from gryffin import Gryffin
..\src\gryffin\__init__.py:3: in <module>
    from .gryffin import Gryffin
..\src\gryffin\gryffin.py:5: in <module>
    from .acquisition import Acquisition
..\src\gryffin\acquisition\__init__.py:3: in <module>
    from .acquisition import Acquisition
..\src\gryffin\acquisition\acquisition.py:11: in <module>
    from .gradient_optimizer import GradientOptimizer
..\src\gryffin\acquisition\gradient_optimizer\__init__.py:6: in <module>
    from .gradient_optimizer import GradientOptimizer
..\src\gryffin\acquisition\gradient_optimizer\gradient_optimizer.py:7: in <module>
    from gryffin.utilities import Logger
..\src\gryffin\utilities\__init__.py:24: in <module>
    from .infos import parse_time, memory_usage, print_memory_usage
..\src\gryffin\utilities\infos.py:3: in <module>
    import resource
E   ModuleNotFoundError: No module named 'resource'
_________________________________________________________________________________________________________ ERROR collecting tests/test_continuous.py __________________________________________________________________________________________________________ 
ImportError while importing test module 'C:\code\ghcwm\gryffin\tests\test_continuous.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\craigmiller\scoop\apps\python310\current\lib\importlib\__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
test_continuous.py:5: in <module>
    from gryffin import Gryffin
..\src\gryffin\__init__.py:3: in <module>
    from .gryffin import Gryffin
..\src\gryffin\gryffin.py:5: in <module>
    from .acquisition import Acquisition
..\src\gryffin\acquisition\__init__.py:3: in <module>
    from .acquisition import Acquisition
..\src\gryffin\acquisition\acquisition.py:11: in <module>
    from .gradient_optimizer import GradientOptimizer
..\src\gryffin\acquisition\gradient_optimizer\__init__.py:6: in <module>
    from .gradient_optimizer import GradientOptimizer
..\src\gryffin\acquisition\gradient_optimizer\gradient_optimizer.py:7: in <module>
    from gryffin.utilities import Logger
..\src\gryffin\utilities\__init__.py:24: in <module>
    from .infos import parse_time, memory_usage, print_memory_usage
..\src\gryffin\utilities\infos.py:3: in <module>
    import resource
E   ModuleNotFoundError: No module named 'resource'
___________________________________________________________________________________________________________ ERROR collecting tests/test_gryffin.py ___________________________________________________________________________________________________________ 
ImportError while importing test module 'C:\code\ghcwm\gryffin\tests\test_gryffin.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\craigmiller\scoop\apps\python310\current\lib\importlib\__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
test_gryffin.py:2: in <module>
    from gryffin import Gryffin
..\src\gryffin\__init__.py:3: in <module>
    from .gryffin import Gryffin
..\src\gryffin\gryffin.py:5: in <module>
    from .acquisition import Acquisition
..\src\gryffin\acquisition\__init__.py:3: in <module>
    from .acquisition import Acquisition
..\src\gryffin\acquisition\acquisition.py:11: in <module>
    from .gradient_optimizer import GradientOptimizer
..\src\gryffin\acquisition\gradient_optimizer\__init__.py:6: in <module>
    from .gradient_optimizer import GradientOptimizer
..\src\gryffin\acquisition\gradient_optimizer\gradient_optimizer.py:7: in <module>
    from gryffin.utilities import Logger
..\src\gryffin\utilities\__init__.py:24: in <module>
    from .infos import parse_time, memory_usage, print_memory_usage
..\src\gryffin\utilities\infos.py:3: in <module>
    import resource
E   ModuleNotFoundError: No module named 'resource'
____________________________________________________________________________________________________________ ERROR collecting tests/test_mixed.py ____________________________________________________________________________________________________________ 
ImportError while importing test module 'C:\code\ghcwm\gryffin\tests\test_mixed.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
C:\Users\craigmiller\scoop\apps\python310\current\lib\importlib\__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
test_mixed.py:5: in <module>
    from gryffin import Gryffin
..\src\gryffin\__init__.py:3: in <module>
    from .gryffin import Gryffin
..\src\gryffin\gryffin.py:5: in <module>
    from .acquisition import Acquisition
..\src\gryffin\acquisition\__init__.py:3: in <module>
    from .acquisition import Acquisition
..\src\gryffin\acquisition\acquisition.py:11: in <module>
    from .gradient_optimizer import GradientOptimizer
..\src\gryffin\acquisition\gradient_optimizer\__init__.py:6: in <module>
    from .gradient_optimizer import GradientOptimizer
..\src\gryffin\acquisition\gradient_optimizer\gradient_optimizer.py:7: in <module>
    from gryffin.utilities import Logger
..\src\gryffin\utilities\__init__.py:24: in <module>
    from .infos import parse_time, memory_usage, print_memory_usage
..\src\gryffin\utilities\infos.py:3: in <module>
    import resource
E   ModuleNotFoundError: No module named 'resource'
================================================================================================================== short test summary info =================================================================================================================== 
ERROR test_categorical.py
ERROR test_constraints.py
ERROR test_continuous.py
ERROR test_gryffin.py
ERROR test_mixed.py
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 5 errors during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 
===================================================================================================================== 5 errors in 21.29s ===================================================================================================================== 
```

</details>

---

### Now we get to the real failures

<details>

```shell
gryffin\tests [ master][!?][🐍 v3.10.11(.gryffin_dev310)]
❯ pytest
==================================================================================================================== test session starts =====================================================================================================================
platform win32 -- Python 3.10.11, pytest-7.4.2, pluggy-1.3.0
rootdir: C:\code\ghcwm\gryffin
collected 12 items

test_categorical.py FFFF                                                                                                                                                                                                                                [ 33%]
test_constraints.py FF                                                                                                                                                                                                                                  [ 50%]
test_continuous.py FF                                                                                                                                                                                                                                   [ 66%]
test_gryffin.py FF                                                                                                                                                                                                                                      [ 83%]
test_mixed.py FF                                                                                                                                                                                                                                        [100%]

========================================================================================================================== FAILURES ==========================================================================================================================
_________________________________________________________________________________________________________________________ test_naive _________________________________________________________________________________________________________________________

    def test_naive():
        param_0_details = {f'x_{i}': None for i in range(NUM_OPTS)} 
        param_1_details  = {f'x_{i}': None for i in range(NUM_OPTS)}
    
        config = {
                "general": {
                        "num_cpus": 4,
                        "auto_desc_gen": False,
                        "batches": 1,
                        "sampling_strategies": 1,
                        "boosted":  False,
                        "caching": True,
                        "random_seed": 2021,
                        "acquisition_optimizer": "adam",
                        "verbosity": 3
                        },
                "parameters": [
                        {"name": "param_0", "type": "categorical", "category_details": param_0_details},
                        {"name": "param_1", "type": "categorical", "category_details": param_1_details},
                ],
                "objectives": [
                        {"name": "obj", "goal": "min"},
                ]
        }

        gryffin = Gryffin(config_dict=config)
        observations = []
        for iter_ in range(BUDGET):
                select_ix = iter_ % len(SAMPLING_STRATEGIES)
                sampling_strategy = SAMPLING_STRATEGIES[select_ix]

>               samples = gryffin.recommend(observations, sampling_strategies=[sampling_strategy])

test_categorical.py:50:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
..\src\gryffin\gryffin.py:374: in recommend
    GB, MB, kB = memory_usage()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

    def memory_usage():
        if sys.platform == 'darwin':  # MacOS --> memory in bytes
            kB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1000.
        else:  # Linux --> memory in kilobytes
>           kB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
E           AttributeError: module 'rsrc' has no attribute 'getrusage'

..\src\gryffin\utilities\infos.py:29: AttributeError
-------------------------------------------------------------------------------------------------------------------- Captured stdout call -------------------------------------------------------------------------------------------------------------------- 
Could not find any observations, falling back to random sampling
________________________________________________________________________________________________________________________ test_static _________________________________________________________________________________________________________________________ 

    def test_static():
        param_0_details = {f'x_{i}': [i] for i in range(NUM_OPTS)}
        param_1_details = {f'x_{i}': [i] for i in range(NUM_OPTS)}

        config = {
                "general": {
                        "num_cpus": 4,
                        "auto_desc_gen": False,
                        "batches": 1,
                        "sampling_strategies": 1,
                        "boosted":  False,
                        "caching": True,
                        "random_seed": 2021,
                        "acquisition_optimizer": "adam",
                        "verbosity": 3
                        },
                "parameters": [
                        {"name": "param_0", "type": "categorical", "category_details": param_0_details},
                        {"name": "param_1", "type": "categorical", "category_details": param_1_details},
                ],
                "objectives": [
                        {"name": "obj", "goal": "min"},
                ]
        }

        gryffin = Gryffin(config_dict=config)
        observations = []
        for iter_ in range(BUDGET):
                select_ix = iter_ % len(SAMPLING_STRATEGIES)
                sampling_strategy = SAMPLING_STRATEGIES[select_ix]

>               samples = gryffin.recommend(observations, sampling_strategies=[sampling_strategy])

test_categorical.py:91:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
..\src\gryffin\gryffin.py:374: in recommend
    GB, MB, kB = memory_usage()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

    def memory_usage():
        if sys.platform == 'darwin':  # MacOS --> memory in bytes
            kB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1000.
        else:  # Linux --> memory in kilobytes
>           kB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
E           AttributeError: module 'rsrc' has no attribute 'getrusage'

..\src\gryffin\utilities\infos.py:29: AttributeError
-------------------------------------------------------------------------------------------------------------------- Captured stdout call -------------------------------------------------------------------------------------------------------------------- 
Could not find any observations, falling back to random sampling
________________________________________________________________________________________________________________________ test_dynamic ________________________________________________________________________________________________________________________ 

    def test_dynamic():
        param_0_details = {f'x_{i}': [i] for i in range(NUM_OPTS)}
        param_1_details = {f'x_{i}': [i] for i in range(NUM_OPTS)}

        config = {
                "general": {
                        "num_cpus": 4,
                        "auto_desc_gen": True,
                        "batches": 1,
                        "sampling_strategies": 1,
                        "boosted":  False,
                        "caching": True,
                        "random_seed": 2021,
                        "acquisition_optimizer": "adam",
                        "verbosity": 3
                        },
                "parameters": [
                        {"name": "param_0", "type": "categorical", "category_details": param_0_details},
                        {"name": "param_1", "type": "categorical", "category_details": param_1_details},
                ],
                "objectives": [
                        {"name": "obj", "goal": "min"},
                ]
        }

        gryffin = Gryffin(config_dict=config)
        observations = []
        for iter_ in range(BUDGET):
                select_ix = iter_ % len(SAMPLING_STRATEGIES)
                sampling_strategy = SAMPLING_STRATEGIES[select_ix]

>               samples = gryffin.recommend(observations, sampling_strategies=[sampling_strategy])

test_categorical.py:133:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
..\src\gryffin\gryffin.py:374: in recommend
    GB, MB, kB = memory_usage()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

    def memory_usage():
        if sys.platform == 'darwin':  # MacOS --> memory in bytes
            kB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1000.
        else:  # Linux --> memory in kilobytes
>           kB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
E           AttributeError: module 'rsrc' has no attribute 'getrusage'

..\src\gryffin\utilities\infos.py:29: AttributeError
-------------------------------------------------------------------------------------------------------------------- Captured stdout call -------------------------------------------------------------------------------------------------------------------- 
Could not find any observations, falling back to random sampling
__________________________________________________________________________________________________________________________ test_moo __________________________________________________________________________________________________________________________ 

    def test_moo():
        param_0_details = {f'x_{i}': [i] for i in range(NUM_OPTS)}
        param_1_details  = {f'x_{i}': [i] for i in range(NUM_OPTS)}

        config = {
                "general": {
                        "num_cpus": 4,
                        "auto_desc_gen": True,
                        "batches": 1,
                        "sampling_strategies": 1,
                        "boosted":  False,
                        "caching": True,
                        "random_seed": 2021,
                        "acquisition_optimizer": "adam",
                        "verbosity": 3
                        },
                "parameters": [
                        {"name": "param_0", "type": "categorical", "category_details": param_0_details},
                        {"name": "param_1", "type": "categorical", "category_details": param_1_details},
                ],
                "objectives": [
                        {"name": "obj_0", "goal": "min", "tolerance": 0.2, "absolute": False},
                        {"name": "obj_1", "goal": "max", "tolerance": 0.1, "absolute": False},
                ]
        }

        gryffin = Gryffin(config_dict=config)
        observations = []
        for iter_ in range(BUDGET):
                select_ix = iter_ % len(SAMPLING_STRATEGIES)
                sampling_strategy = SAMPLING_STRATEGIES[select_ix]

>               samples = gryffin.recommend(observations, sampling_strategies=[sampling_strategy])

test_categorical.py:175:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
..\src\gryffin\gryffin.py:374: in recommend
    GB, MB, kB = memory_usage()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

    def memory_usage():
        if sys.platform == 'darwin':  # MacOS --> memory in bytes
            kB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1000.
        else:  # Linux --> memory in kilobytes
>           kB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
E           AttributeError: module 'rsrc' has no attribute 'getrusage'

..\src\gryffin\utilities\infos.py:29: AttributeError
-------------------------------------------------------------------------------------------------------------------- Captured stdout call -------------------------------------------------------------------------------------------------------------------- 
Could not find any observations, falling back to random sampling
___________________________________________________________________________________________________________________ test_constraints_cont ____________________________________________________________________________________________________________________ 

    def test_constraints_cont():
        # frac_feas roughly 0.5552
        config = {
                "general": {
                        "num_cpus": 4,
                        "auto_desc_gen": False,
                        "batches": 1,
                        "sampling_strategies": 1,
                        "boosted":  False,
                        "caching": True,
                        "random_seed": 2021,
                        "acquisition_optimizer": "adam",
                        "verbosity": 3
                        },
                "parameters": [
                        {"name": "param_0", "type": "continuous", "low": 0., "high": 1.},
                        {"name": "param_1", "type": "continuous", "low": 0., "high": 1.},
                ],
                "objectives": [
                        {"name": "obj", "goal": "min"},
                ]
        }

        gryffin = Gryffin(
                config_dict=config, known_constraints=known_constraints_cont,
        )
        # check if the estimated feasible reagion is reasonably accurate
        delta = 1.e-3
        assert 0.5552-delta <= gryffin.frac_feas <= 0.5552+delta
        observations = []
        for iter_ in range(BUDGET):
                select_ix = iter_ % len(SAMPLING_STRATEGIES)
                sampling_strategy = SAMPLING_STRATEGIES[select_ix]

>               samples = gryffin.recommend(observations, sampling_strategies=[sampling_strategy])

test_constraints.py:85:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
..\src\gryffin\gryffin.py:374: in recommend
    GB, MB, kB = memory_usage()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

    def memory_usage():
        if sys.platform == 'darwin':  # MacOS --> memory in bytes
            kB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1000.
        else:  # Linux --> memory in kilobytes
>           kB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
E           AttributeError: module 'rsrc' has no attribute 'getrusage'

..\src\gryffin\utilities\infos.py:29: AttributeError
-------------------------------------------------------------------------------------------------------------------- Captured stdout call -------------------------------------------------------------------------------------------------------------------- 
Could not find any observations, falling back to random sampling
____________________________________________________________________________________________________________________ test_constraints_cat ____________________________________________________________________________________________________________________ 

    def test_constraints_cat():
        # frac_feas = FRAC FEAS :  0.7324263038548753
        param_0_details = {f'x_{i}': [i] for i in range(NUM_OPTS)}
        param_1_details  = {f'x_{i}': [i] for i in range(NUM_OPTS)}

        config = {
                "general": {
                        "num_cpus": 4,
                        "auto_desc_gen": True,
                        "batches": 1,
                        "sampling_strategies": 1,
                        "boosted":  False,
                        "caching": True,
                        "random_seed": 2021,
                        "acquisition_optimizer": "adam",
                        "verbosity": 3
                        },
                "parameters": [
                        {"name": "param_0", "type": "categorical", "category_details": param_0_details},
                        {"name": "param_1", "type": "categorical", "category_details": param_1_details},
                ],
                "objectives": [
                        {"name": "obj", "goal": "min"},
                ]
        }

        gryffin = Gryffin(
                config_dict=config, known_constraints=known_constraints_cat
        )
        # check if the estimated feasible reagion is reasonably accurate
        delta = 1.e-6
        assert 0.7324263038548753-delta <= gryffin.frac_feas <= 0.7324263038548753+delta
        observations = []
        for iter_ in range(BUDGET):
                select_ix = iter_ % len(SAMPLING_STRATEGIES)
                sampling_strategy = SAMPLING_STRATEGIES[select_ix]

>               samples = gryffin.recommend(observations, sampling_strategies=[sampling_strategy])

test_constraints.py:135:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
..\src\gryffin\gryffin.py:374: in recommend
    GB, MB, kB = memory_usage()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

    def memory_usage():
        if sys.platform == 'darwin':  # MacOS --> memory in bytes
            kB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1000.
        else:  # Linux --> memory in kilobytes
>           kB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
E           AttributeError: module 'rsrc' has no attribute 'getrusage'

..\src\gryffin\utilities\infos.py:29: AttributeError
-------------------------------------------------------------------------------------------------------------------- Captured stdout call -------------------------------------------------------------------------------------------------------------------- 
Could not find any observations, falling back to random sampling
_________________________________________________________________________________________________________________________ test_cont __________________________________________________________________________________________________________________________ 

    def test_cont():
        config = {
                "general": {
                        "num_cpus": 4,
                        "auto_desc_gen": False,
                        "batches": 1,
                        "sampling_strategies": 1,
                        "boosted":  False,
                        "caching": True,
                        "random_seed": 2021,
                        "acquisition_optimizer": "adam",
                        "verbosity": 3
                        },
                "parameters": [
                        {"name": "param_0", "type": "continuous", "low": 0., "high": 1.},
                        {"name": "param_1", "type": "continuous", "low": 0., "high": 1.},
                ],
                "objectives": [
                        {"name": "obj", "goal": "min"},
                ]
        }

        gryffin = Gryffin(config_dict=config)
        observations = []
        for iter_ in range(BUDGET):
                select_ix = iter_ % len(SAMPLING_STRATEGIES)
                sampling_strategy = SAMPLING_STRATEGIES[select_ix]

>               samples = gryffin.recommend(observations, sampling_strategies=[sampling_strategy])

test_continuous.py:44:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
..\src\gryffin\gryffin.py:374: in recommend
    GB, MB, kB = memory_usage()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

    def memory_usage():
        if sys.platform == 'darwin':  # MacOS --> memory in bytes
            kB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1000.
        else:  # Linux --> memory in kilobytes
>           kB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
E           AttributeError: module 'rsrc' has no attribute 'getrusage'

..\src\gryffin\utilities\infos.py:29: AttributeError
-------------------------------------------------------------------------------------------------------------------- Captured stdout call -------------------------------------------------------------------------------------------------------------------- 
Could not find any observations, falling back to random sampling
__________________________________________________________________________________________________________________________ test_moo __________________________________________________________________________________________________________________________ 

    def test_moo():
        config = {
                "general": {
                        "num_cpus": 4,
                        "auto_desc_gen": False,
                        "batches": 1,
                        "sampling_strategies": 1,
                        "boosted":  False,
                        "caching": True,
                        "random_seed": 2021,
                        "acquisition_optimizer": "adam",
                        "verbosity": 3
                        },
                "parameters": [
                        {"name": "param_0", "type": "continuous", "low": 0., "high": 1.},
                        {"name": "param_1", "type": "continuous", "low": 0., "high": 1.},
                ],
                "objectives": [
                        {"name": "obj_0", "goal": "min", "tolerance": 0.2, "absolute": False},
                        {"name": "obj_1", "goal": "max", "tolerance": 0.1, "absolute": False},
                ]
        }

        gryffin = Gryffin(config_dict=config)
        observations = []
        for iter_ in range(BUDGET):
                select_ix = iter_ % len(SAMPLING_STRATEGIES)
                sampling_strategy = SAMPLING_STRATEGIES[select_ix]

>               samples = gryffin.recommend(observations, sampling_strategies=[sampling_strategy])

test_continuous.py:83:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
..\src\gryffin\gryffin.py:374: in recommend
    GB, MB, kB = memory_usage()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

    def memory_usage():
        if sys.platform == 'darwin':  # MacOS --> memory in bytes
            kB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1000.
        else:  # Linux --> memory in kilobytes
>           kB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
E           AttributeError: module 'rsrc' has no attribute 'getrusage'

..\src\gryffin\utilities\infos.py:29: AttributeError
-------------------------------------------------------------------------------------------------------------------- Captured stdout call -------------------------------------------------------------------------------------------------------------------- 
Could not find any observations, falling back to random sampling
_______________________________________________________________________________________________________________________ test_recommend _______________________________________________________________________________________________________________________ 

    def test_recommend():
        config = {
            "general": {
                "save_database": False,
                "num_cpus": 1,
                "boosted": True,
                "sampling_strategies": 2,
                "random_seed": 42,
            },
            "parameters": [{"name": "param_0", "type": "continuous", "low": 0, "high": 1},
                           {"name": "param_1", "type": "continuous", "low": 0, "high": 1}],
            "objectives": [{"name": "obj", "goal": "min"}]
            }

        observations = [
            {'param_0': 0.3, 'param_1': 0.4, 'obj': 0.1},
            {'param_0': 0.5, 'param_1': 0.6, 'obj': 0.2},
        ]

        gryffin = Gryffin(config_dict=config)
>       _ = gryffin.recommend(observations=observations)

test_gryffin.py:27:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
..\src\gryffin\gryffin.py:321: in recommend
    self.bayesian_network.build_kernels(descriptors_kwn=descriptors_kwn, descriptors_feas=descriptors_feas,
..\src\gryffin\bayesian_network\bayesian_network.py:151: in build_kernels
    probs_kwn = self._reshape_categorical_probabilities(probs_kwn, descriptors_kwn)
..\src\gryffin\bayesian_network\bayesian_network.py:226: in _reshape_categorical_probabilities
    if np.all(np.isfinite(np.array(descriptors, dtype=np.float))):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

attr = 'float'

    def __getattr__(attr):
        # Warn for expired attributes, and return a dummy function
        # that always raises an exception.
        import warnings
        import math
        try:
            msg = __expired_functions__[attr]
        except KeyError:
            pass
        else:
            warnings.warn(msg, DeprecationWarning, stacklevel=2)

            def _expired(*args, **kwds):
                raise RuntimeError(msg)

            return _expired

        # Emit warnings for deprecated attributes
        try:
            val, msg = __deprecated_attrs__[attr]
        except KeyError:
            pass
        else:
            warnings.warn(msg, DeprecationWarning, stacklevel=2)
            return val

        if attr in __future_scalars__:
            # And future warnings for those that will change, but also give
            # the AttributeError
            warnings.warn(
                f"In the future `np.{attr}` will be defined as the "
                "corresponding NumPy scalar.", FutureWarning, stacklevel=2)

        if attr in __former_attrs__:
>           raise AttributeError(__former_attrs__[attr])
E           AttributeError: module 'numpy' has no attribute 'float'.
E           `np.float` was a deprecated alias for the builtin `float`. To avoid this error in existing code, use `float` by itself. Doing this will not modify any behavior and is safe. If you specifically wanted the numpy scalar type, use `np.float64` here.
E           The aliases was originally deprecated in NumPy 1.20; for more details and guidance see the original release note at:
E               https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations. Did you mean: 'cfloat'?

..\.gryffin_dev310\lib\site-packages\numpy\__init__.py:338: AttributeError
-------------------------------------------------------------------------------------------------------------------- Captured stdout call -------------------------------------------------------------------------------------------------------------------- 

=================================== Gryffin
====================================
Gryffin will propose 2 samples: 1 batch with 2 sampling strategies
2 observations found
─────────────────────────────── Bayesian Network
───────────────────────────────
Bayesian neural network trained in 9.6 s
____________________________________________________________________________________________________________________ test_multiobjective _____________________________________________________________________________________________________________________ 

    def test_multiobjective():
        config = {
            "general": {
                "save_database": False,
                "num_cpus": 1,
                "boosted": True,
                "sampling_strategies": 2,
                "random_seed": 42,
            },
            "parameters": [{"name": "param_0", "type": "continuous", "low": 0, "high": 1},
                           {"name": "param_1", "type": "continuous", "low": 0, "high": 1}],
            "objectives": [{"name": "obj0", "goal": "min", "tolerance": 0.2, "absolute": False},
                           {"name": "obj1", "goal": "max", "tolerance": 0.1, "absolute": False}]
        }

        observations = [
            {'param_0': 0.3, 'param_1': 0.4, 'obj0': 0.1, 'obj1': 0.2},
            {'param_0': 0.5, 'param_1': 0.6, 'obj0': 0.2, 'obj1': 0.1},
        ]

        gryffin = Gryffin(config_dict=config)
>       _ = gryffin.recommend(observations=observations)

test_gryffin.py:51:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
..\src\gryffin\gryffin.py:321: in recommend
    self.bayesian_network.build_kernels(descriptors_kwn=descriptors_kwn, descriptors_feas=descriptors_feas,
..\src\gryffin\bayesian_network\bayesian_network.py:151: in build_kernels
    probs_kwn = self._reshape_categorical_probabilities(probs_kwn, descriptors_kwn)
..\src\gryffin\bayesian_network\bayesian_network.py:226: in _reshape_categorical_probabilities
    if np.all(np.isfinite(np.array(descriptors, dtype=np.float))):
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

attr = 'float'

    def __getattr__(attr):
        # Warn for expired attributes, and return a dummy function
        # that always raises an exception.
        import warnings
        import math
        try:
            msg = __expired_functions__[attr]
        except KeyError:
            pass
        else:
            warnings.warn(msg, DeprecationWarning, stacklevel=2)

            def _expired(*args, **kwds):
                raise RuntimeError(msg)

            return _expired

        # Emit warnings for deprecated attributes
        try:
            val, msg = __deprecated_attrs__[attr]
        except KeyError:
            pass
        else:
            warnings.warn(msg, DeprecationWarning, stacklevel=2)
            return val

        if attr in __future_scalars__:
            # And future warnings for those that will change, but also give
            # the AttributeError
            warnings.warn(
                f"In the future `np.{attr}` will be defined as the "
                "corresponding NumPy scalar.", FutureWarning, stacklevel=2)

        if attr in __former_attrs__:
>           raise AttributeError(__former_attrs__[attr])
E           AttributeError: module 'numpy' has no attribute 'float'.
E           `np.float` was a deprecated alias for the builtin `float`. To avoid this error in existing code, use `float` by itself. Doing this will not modify any behavior and is safe. If you specifically wanted the numpy scalar type, use `np.float64` here.
E           The aliases was originally deprecated in NumPy 1.20; for more details and guidance see the original release note at:
E               https://numpy.org/devdocs/release/1.20.0-notes.html#deprecations. Did you mean: 'cfloat'?

..\.gryffin_dev310\lib\site-packages\numpy\__init__.py:338: AttributeError
-------------------------------------------------------------------------------------------------------------------- Captured stdout call -------------------------------------------------------------------------------------------------------------------- 

=================================== Gryffin
====================================
Gryffin will propose 2 samples: 1 batch with 2 sampling strategies
2 observations found
─────────────────────────────── Bayesian Network
───────────────────────────────
Bayesian neural network trained in 9.0 s
_________________________________________________________________________________________________________________________ test_mixed _________________________________________________________________________________________________________________________ 

    def test_mixed():
        param_2_details = {f'x_{i}': [i] for i in range(NUM_OPTS)}
        config = {
                "general": {
                        "num_cpus": 4,
                        "auto_desc_gen": True,
                        "batches": 1,
                        "sampling_strategies": 1,
                        "boosted":  False,
                        "caching": True,
                        "random_seed": 2021,
                        "acquisition_optimizer": "adam",
                        "verbosity": 3
                        },
                "parameters": [
                        {"name": "param_0", "type": "continuous", "low": 0., "high": 1.},
                        {"name": "param_1", "type": "continuous", "low": 0., "high": 1.},
                        {"name": "param_2", "type": "categorical", "category_details": param_2_details},
                ],
                "objectives": [
                        {"name": "obj", "goal": "min"},
                ]
        }

        gryffin = Gryffin(config_dict=config)
        observations = []
        for iter_ in range(BUDGET):
                select_ix = iter_ % len(SAMPLING_STRATEGIES)
                sampling_strategy = SAMPLING_STRATEGIES[select_ix]

>               samples = gryffin.recommend(observations, sampling_strategies=[sampling_strategy])

test_mixed.py:48:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
..\src\gryffin\gryffin.py:374: in recommend
    GB, MB, kB = memory_usage()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

    def memory_usage():
        if sys.platform == 'darwin':  # MacOS --> memory in bytes
            kB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1000.
        else:  # Linux --> memory in kilobytes
>           kB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
E           AttributeError: module 'rsrc' has no attribute 'getrusage'

..\src\gryffin\utilities\infos.py:29: AttributeError
-------------------------------------------------------------------------------------------------------------------- Captured stdout call -------------------------------------------------------------------------------------------------------------------- 
Could not find any observations, falling back to random sampling
__________________________________________________________________________________________________________________________ test_moo __________________________________________________________________________________________________________________________ 

    def test_moo():
        param_2_details = {f'x_{i}': [i] for i in range(NUM_OPTS)}
        config = {
                "general": {
                        "num_cpus": 4,
                        "auto_desc_gen": True,
                        "batches": 1,
                        "sampling_strategies": 1,
                        "boosted":  False,
                        "caching": True,
                        "random_seed": 2021,
                        "acquisition_optimizer": "adam",
                        "verbosity": 3
                        },
                "parameters": [
                        {"name": "param_0", "type": "continuous", "low": 0., "high": 1.},
                        {"name": "param_1", "type": "continuous", "low": 0., "high": 1.},
                        {"name": "param_2", "type": "categorical", "category_details": param_2_details},
                ],
                "objectives": [
                        {"name": "obj_0", "goal": "min", "tolerance": 0.2, "absolute": False},
                        {"name": "obj_1", "goal": "max", "tolerance": 0.1, "absolute": False},
                ]
        }

        gryffin = Gryffin(config_dict=config)
        observations = []
        for iter_ in range(BUDGET):
                select_ix = iter_ % len(SAMPLING_STRATEGIES)
                sampling_strategy = SAMPLING_STRATEGIES[select_ix]

>               samples = gryffin.recommend(observations, sampling_strategies=[sampling_strategy])

test_mixed.py:92: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  
..\src\gryffin\gryffin.py:374: in recommend
    GB, MB, kB = memory_usage()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

    def memory_usage():
        if sys.platform == 'darwin':  # MacOS --> memory in bytes
            kB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss // 1000.
        else:  # Linux --> memory in kilobytes
>           kB = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
E           AttributeError: module 'rsrc' has no attribute 'getrusage'

..\src\gryffin\utilities\infos.py:29: AttributeError
-------------------------------------------------------------------------------------------------------------------- Captured stdout call -------------------------------------------------------------------------------------------------------------------- 
Could not find any observations, falling back to random sampling
====================================================================================================================== warnings summary ====================================================================================================================== 
..\src\gryffin\sample_selector\sample_selector.py:202
  C:\code\ghcwm\gryffin\src\gryffin\sample_selector\sample_selector.py:202: SyntaxWarning: "is not" with a literal. Did you mean "!="?
    if self.problem_type is not 'fully_categorical':

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
================================================================================================================== short test summary info =================================================================================================================== 
FAILED test_categorical.py::test_naive - AttributeError: module 'rsrc' has no attribute 'getrusage'
FAILED test_categorical.py::test_static - AttributeError: module 'rsrc' has no attribute 'getrusage'
FAILED test_categorical.py::test_dynamic - AttributeError: module 'rsrc' has no attribute 'getrusage'
FAILED test_categorical.py::test_moo - AttributeError: module 'rsrc' has no attribute 'getrusage'
FAILED test_constraints.py::test_constraints_cont - AttributeError: module 'rsrc' has no attribute 'getrusage'
FAILED test_constraints.py::test_constraints_cat - AttributeError: module 'rsrc' has no attribute 'getrusage'
FAILED test_continuous.py::test_cont - AttributeError: module 'rsrc' has no attribute 'getrusage'
FAILED test_continuous.py::test_moo - AttributeError: module 'rsrc' has no attribute 'getrusage'
FAILED test_gryffin.py::test_recommend - AttributeError: module 'numpy' has no attribute 'float'.
FAILED test_gryffin.py::test_multiobjective - AttributeError: module 'numpy' has no attribute 'float'.
FAILED test_mixed.py::test_mixed - AttributeError: module 'rsrc' has no attribute 'getrusage'
FAILED test_mixed.py::test_moo - AttributeError: module 'rsrc' has no attribute 'getrusage'
========================================================================================================== 12 failed, 1 warning in 87.62s (0:01:27) ========================================================================================================== 

gryffin\tests [ master][!?][🐍 v3.10.11(.gryffin_dev310)][⏱ 1m46s]
❯
```

</details>

---
