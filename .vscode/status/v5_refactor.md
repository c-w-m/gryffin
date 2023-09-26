# `resource` Refactor

## Refactor `infos.py`

## New Development Installation

```shell
gryffin [ master][!?][🐍 v3.8.8]
> cd C:\code\ghcwm\gryffin
> python310 -m venv .gryffin_dev310
> .\.gryffin_dev310\Scripts\activate.bat

gryffin [ master][!?][🐍 v3.10.11(.gryffin_dev310)]
> python -m pip install --upgrade pip
> pip install -e .
```

<details>

```shell
> pip install -e .

Looking in indexes: https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/simple
Obtaining file:///C:/code/ghcwm/gryffin
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Preparing editable metadata (pyproject.toml) ... done
Collecting psutil (from gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/86/f3/23e4e4e7ec7855d506ed928756b04735c246b14d9f778ed7ffaae18d8043/psutil-5.9.5-cp36-abi3-win_amd64.whl (255 kB)
Collecting numpy (from gryffin==0+untagged.325.g8696bf8.dirty)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/cc/05/ef9fc04adda45d537619ea956bc33489f50a46badc949c4280d8309185ec/numpy-1.26.0-cp310-cp310-win_amd64.whl (15.8 MB)
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
  Created wheel for gryffin: filename=gryffin-0+untagged.325.g8696bf8.dirty-0.editable-cp310-cp310-win_amd64.whl size=7954 sha256=6624f23fa4648ad60e5dace9bda1d2395fe03d3f237532eacfc9c912fc4548cb
  Stored in directory: C:\Users\craigmiller\AppData\Local\Temp\pip-ephem-wheel-cache-4ubf93ii\wheels\e3\e7\a8\bad0faefb603dcc7c3c5d75c3af158a50199aa8b2ea6c64c3a

Successfully built gryffin

Installing collected packages: pytz, mpmath, tzdata, typing-extensions, torchbnn, sympy, six, pygments, psutil, numpy, networkx, mdurl, MarkupSafe, greenlet, filelock, sqlalchemy, python-dateutil, matter-chimera, markdown-it-py, jinja2, deap, torch, rich, pandas, gryffin

Successfully installed MarkupSafe-2.1.3 deap-1.4.1 filelock-3.12.4 greenlet-2.0.2 gryffin-0+untagged.325.g8696bf8.dirty jinja2-3.1.2 markdown-it-py-3.0.0 matter-chimera-1.0 mdurl-0.1.2 mpmath-1.3.0 networkx-3.1 numpy-1.26.0 pandas-2.1.1 psutil-5.9.5 pygments-2.16.1 python-dateutil-2.8.2 pytz-2023.3.post1 rich-13.5.3 six-1.16.0 sqlalchemy-2.0.21 sympy-1.12 torch-2.0.1 torchbnn-1.2 typing-extensions-4.8.0 tzdata-2023.3

gryffin [ master][!?][🐍 v3.10.11(.gryffin_dev310)][⏱ 15m16s]
```

</details>

---

### `pytest`

```shell
gryffin\tests [ master][!?][🐍 v3.10.11(.gryffin_dev310)]
❯ pip install pytest
```

<details>

```shell
gryffin [ master][!?][🐍 v3.10.11(.gryffin_dev310)]
❯ pip install pytest
Looking in indexes: https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/simple
Collecting pytest
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/df/d0/e192c4275aecabf74faa1aacd75ef700091913236ec78b1a98f62a2412ee/pytest-7.4.2-py3-none-any.whl (324 kB)
Collecting iniconfig (from pytest)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/ef/a6/62565a6e1cf69e10f5727360368e451d4b7f58beeac6173dc9db836a5b46/iniconfig-2.0.0-py3-none-any.whl (5.9 kB)
Collecting packaging (from pytest)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/ab/c3/57f0601a2d4fe15de7a553c00adbc901425661bf048f2a22dfc500caf121/packaging-23.1-py3-none-any.whl (48 kB)
Collecting pluggy<2.0,>=0.12 (from pytest)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/05/b8/42ed91898d4784546c5f06c60506400548db3f7a4b3fb441cba4e5c17952/pluggy-1.3.0-py3-none-any.whl (18 kB)
Collecting exceptiongroup>=1.0.0rc8 (from pytest)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/ad/83/b71e58666f156a39fb29417e4c8ca4bc7400c0dd4ed9e8842ab54dc8c344/exceptiongroup-1.1.3-py3-none-any.whl (14 kB)
Collecting tomli>=1.0.0 (from pytest)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/97/75/10a9ebee3fd790d20926a90a2547f0bf78f371b2f13aa822c759680ca7b9/tomli-2.0.1-py3-none-any.whl (12 kB)
Collecting colorama (from pytest)
  Using cached https://artifactory.micron.com/artifactory/api/pypi/zextpythonorg-pypi-rel-remote/packages/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl (25 kB)

Installing collected packages: tomli, pluggy, packaging, iniconfig, exceptiongroup, colorama, pytest

Successfully installed colorama-0.4.6 exceptiongroup-1.1.3 iniconfig-2.0.0 packaging-23.1 pluggy-1.3.0 pytest-7.4.2 tomli-2.0.1

gryffin [ master][!?][🐍 v3.10.11(.gryffin_dev310)][⏱ 41s]
```

</details>

---
