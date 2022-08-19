#! /usr/bin/env python
# Enable Developer Mode

import os
import platform

from pathlib import Path


class RokuRemote:
  commands = {
    'UP': [0,8982,4486,550,560,524,1657,549,576,508,1658,548,561,523,1656,550,1654,552,1656,550,560,524,1656,550,562,522,563,521,565,519,564,520,1659,547,1659,556,1650,546,566,518,565,520,1660,546,1660,545,566,518,568,526,560,524,560,524,1654,552,1655,551,561,523,560,524,1655,551,1654,551,1653,543],

    'DOWN': [0,8989,4478,548,535,549,1658,548,536,548,1658,548,535,549,1656,550,1654,551,1656,550,534,550,1656,550,535,549,537,547,538,546,538,546,1658,548,1658,547,1657,550,1657,548,537,547,537,547,1658,548,1658,564,522,546,540,545,541,543,541,543,1662,544,1662,544,542,552,531,542,1664,542,1662,544],

    'LEFT': [0,8985,4480,546,537,547,1660,545,538,546,1661,545,538,546,1658,548,1657,548,1659,546,537,547,1660,545,540,544,542,556,529,552,531,552,1653,543,1664,552,531,552,1653,543,1661,544,1660,546,1660,545,540,543,542,553,532,551,1655,551,534,550,535,549,537,546,537,547,1657,548,1656,550,1655,551],

    'RIGHT': [0,8983,4483,543,541,557,1649,543,541,543,1663,544,540,544,1660,546,1659,547,1660,545,538,546,1660,546,540,544,541,542,543,552,531,553,1677,518,1662,544,1662,543,540,544,1661,545,1661,544,539,545,1662,543,542,542,544,550,534,550,1656,550,536,548,535,549,1657,548,536,548,1656,550,1655,551],

    'SELECT': [0,8985,4481,546,538,546,1661,546,538,546,1661,545,539,545,1660,546,1659,548,1659,547,537,547,1659,547,539,545,541,543,542,575,509,543,1662,544,1664,542,541,544,1663,560,523,544,1663,543,540,544,1663,543,543,552,532,552,1655,551,532,552,1655,551,533,552,1655,551,532,552,1653,543,1661,545],

    'BACK': [0,8986,4479,547,537,547,1660,546,537,548,1659,547,536,548,1657,549,1656,551,1657,552,532,549,1658,580,506,547,538,577,509,544,539,546,1659,578,1630,576,508,545,1660,547,1659,578,508,545,539,576,1628,579,1628,578,507,577,1630,577,508,576,508,545,1659,578,1629,577,509,584,499,577,1628,547],

    'HOME': [0,8987,4475,551,558,526,1654,552,557,527,1653,553,556,519,1659,545,1659,546,1661,545,564,520,1659,546,565,519,567,517,568,526,569,504,1661,545,1659,546,1658,547,1664,542,537,546,539,545,540,544,541,553,530,544,1664,551,546,538,533,551,1653,552,1651,544,1659,547,1657,548,1658,548,535,570]
  }

  def __init__(self):
    project_dir = Path().resolve()
    flirc = {
      'darwin': str(Path(project_dir / "bin/darwin/flirc_util")),
    }
    self.bin = flirc[platform.system().lower()]
    print(self.bin)


  def code_to_string(self, command):
    # TODO: build_command()
    # flirc_util.exe sendir --ik=23000 --repeat=3 --pattern
    return ','.join([str(i) for i in command])


  def send_command(self, command):
    cmd = self.code_to_string(command)
    flirc_command = f"{self.bin} sendir --pattern={cmd}"
    return os.popen(flirc_command).read()


  def enable_developer_mode(self):
    macro = [
      "HOME", "HOME", "HOME",
      "UP", "UP",
      "RIGHT", "LEFT",
      "RIGHT", "LEFT",
      "RIGHT"
      "SELECT"
    ]
    for key in macro:
      self.send_command(self.commands[key])


remote = RokuRemote()
remote.enable_developer_mode()
