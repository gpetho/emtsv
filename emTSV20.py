#!/usr/bin/python3
# -*- coding: utf-8, vim: expandtab:ts=4 -*-

import sys

from emTSV20_common import init_everything, build_pipeline, pipeline_rest_api
from config import tools, presets

if __name__ == '__main__':
    if len(sys.argv) > 1:  # TODO: Implement this properly = Argparse
        if sys.argv[1] in presets:
            used_tools = presets[sys.argv[1]]
        else:
            used_tools = sys.argv[1].split(',')
        required_tools = set(used_tools)
        inited_tools = init_everything({k: v for k, v in tools.items() if k in required_tools})
        sys.stdout.writelines(build_pipeline(sys.stdin, used_tools, inited_tools))
    else:
        inited_tools = init_everything(tools)
        app = pipeline_rest_api(inited_tools, name='emTSV20')
        app.run(debug=True)
