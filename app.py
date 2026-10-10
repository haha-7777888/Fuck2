#
# Copyright (C) 2021-2022 by TheAloneteam@Github, < https://github.com/TheAloneTeam >.
# This file is part of < https://github.com/TheAloneTeam/ZeroTwo > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheAloneTeam/ZeroTwo/blob/master/LICENSE >
#
# All rights reserved.

import sys

print("🚀 Starting ZeroTwo Bot...")

try:
    # Run the package as module
    import runpy

    runpy.run_module("ZeroTwo", run_name="__main__")
except Exception as e:
    print("❌ Bot crashed with error:", e)
    sys.exit(1)
