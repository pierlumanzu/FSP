import os
import subprocess

from config import OUTPUT_PATH


HEADER = "\documentclass{{article}}\n \
          \\usepackage{{multirow}}\n \
          \\begin{{document}}\n\n \
          \\setlength{{\\tabcolsep}}{{2pt}} \n \
          \\begin{{table}}[htb]\n \
          \\begin{{tabular}}{{|{}}} \n \
              \hline \n \
              \multirow{{2}}{{*}}{{Problem}} &"

FOOTER = "  \end{{tabular}}\n \
          \end{{table}}\n\n \
          \end{{document}}"

FIELD_NAMES = [r'$f^\star$', r'$n_f$', r'$n_p$']
FIELD_FORMATS = [':.3f', ':d', ':d']
FIELD_FNCS = [lambda p: float(p['f_xbar']), lambda p: int(p['nf']), lambda p: int(p['np'])]


def create_table(results: dict) :
    assert len(FIELD_NAMES) == len(FIELD_FORMATS) == len(FIELD_FNCS)
    n_fields = len(FIELD_NAMES)

    solvers = list(results.keys())
    problems = list(results[solvers[0]].keys())

    space = '       '

    header = HEADER.format('c|' * (len(solvers) * n_fields + 1))
    header += " & ".join(['\multicolumn{{{}}}{{c|}}{{{}}}'.format(n_fields, s) for s in solvers])
    # header += ' & \multicolumn{{{}}}{{c|}}{{{}}}'.format(n_fields, solvers[-1])
    header += "\\\\\n"
    header += space + "\cline{2-" + str(len(solvers) * n_fields + 1) + "}\n"
    header += space + "& " + " & ".join([" & ".join(FIELD_NAMES) for i in range(len(solvers))]) + "  \\\\\n"
    header += space + "\hline\n"

    body = ""
    for p in problems:
        
        body += space + p + "& "
        v = []
        
        for s in solvers:
            for i in range(n_fields):
                v.append(("{" + FIELD_FORMATS[i] + "}").format(FIELD_FNCS[i](results[s][p])))
        
        body += " & ".join(v) + " \\\\\n"
        body += space + "\hline\n"

    with open(os.path.join(OUTPUT_PATH, 'benchmark_table.tex'), 'w') as f:
        f.writelines([header + body + FOOTER.format()])

    try:
        subprocess.run(["latexmk", "-pdf", "-output-directory=" + OUTPUT_PATH, os.path.join(OUTPUT_PATH, 'benchmark_table.tex')], check=True)
        subprocess.run(["rm", "{}benchmark_table.aux".format(OUTPUT_PATH), 
                              "{}benchmark_table.fdb_latexmk".format(OUTPUT_PATH),
                              "{}benchmark_table.fls".format(OUTPUT_PATH),
                              "{}benchmark_table.log".format(OUTPUT_PATH)], check=True)
        print(f"Compilation successful!")
    except subprocess.CalledProcessError as e:
        print("Error during compilation of Tex file:", e)
