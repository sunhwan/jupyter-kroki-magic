import requests
import os
from enum import Enum
from IPython.core.magic import Magics, cell_magic, magics_class
from IPython.display import SVG, display
from IPython.core.magic_arguments import (argument, magic_arguments,
                                        parse_argstring)
from argparse import BooleanOptionalAction

# TODO: get diagram types from <KROKI_ENDPOINT>/health
class DiagramType(str, Enum):
    actdiag="actdiag"
    blockdiag="blockdiag"
    bpmn="bpmn"
    bytefield="bytefield"
    c4plantuml="c4plantuml"
    d2="d2"
    dbml="dbml"
    diagramsnet="diagramsnet"
    ditaa="ditaa"
    dot="dot"
    erd="erd"
    excalidraw="excalidraw"
    graphviz="graphviz"
    kroki="kroki"
    mermaid="mermaid"
    nomnoml="nomnoml"
    nwdiag="nwdiag"
    packetdiag="packetdiag"
    pikchr="pikchr"
    plantuml="plantuml"
    rackdiag="rackdiag"
    seqdiag="seqdiag"
    structurizr="structurizr"
    svgbob="svgbob"
    umlet="umlet"
    vega="vega"
    vegalite="vegalite"
    wavedrom="wavedrom"

@magics_class
class KrokiMagic(Magics):
    
    @cell_magic
    @magic_arguments()
    @argument('type', type=DiagramType, help=f'required kroki diagram type, one of {DiagramType._member_names_}')
    @argument('--url', '-u', help="URL of kroki server to be used, defaults to os.env['KROKI_ENDPOINT'] and if not set to https://kroki.io]", default=os.getenv('KROKI_ENDPOINT', "https://kroki.io"))
    @argument('--ssl', action=BooleanOptionalAction, help="verify ssl chain", default=True)
    @argument('--expand_vars', action=BooleanOptionalAction, metavar="--expand-vars", help="replace/expand variables from user namespace within cell content before sending to kroki", default=False)
    def kroki(self, line, cell):
        
        
        args = parse_argstring(self.kroki, line)

        content= cell.format(**self.shell.user_ns) if args.expand_vars else cell
        
        if not args.ssl:
            requests.packages.urllib3.disable_warnings() 
        r = requests.post(f'{args.url}/{args.type}/svg', json={'diagram_source': content}, verify=False)
        if r.status_code == 200:
            return display(SVG(r.text))
        else:
            print(r.status_code, r.text)
            raise ValueError