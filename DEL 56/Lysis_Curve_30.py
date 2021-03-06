import os
from matplotlib import pyplot as plt
from analysis import analyse_file, gen_pair_graphs

#####################
##     GROUP 1     ##
#####################

for rept in [1,2,3,4]:
    deg = 30
    # deg = 37
    # rept = 4
    time_in_oven = 12
    csv_filename = f'{deg}deg_{rept}_repeat'
    groups_filename = 'group1'
    output_folder = f'lysis_curve_4_repeats'

    df = analyse_file(
        opticalDense_path = f'./csv/{csv_filename}.csv',
        triplicates_path  = f'./groups/{groups_filename}.csv',
        blanks            = ['A3', 'A9'],
        parse_time        = True,
    )
    figs = {}

    ## WT ##
    title = f'Lysis Curve - {deg}°C\nWT'
    cols = [ c for c in df.columns if 'WT' in c ]
    fig,axs = gen_pair_graphs(df, cols, title, xticks=range(time_in_oven+1))
    title = title.split('\n')
    figs[title[1]] = fig
    ## WT ##

    wt_cols = [ c for c in df.columns if 'WT' in c and 'd_01556' not in c ]
    wt_del_cols = [ c for c in df.columns if 'WT' in c and 'd_01556' in c ]

    ## struc ##
    title = f'Lysis Curve - {deg}°C\nΔstruc'
    cols = wt_cols + [ c for c in df.columns if 'struc' in c ]
    fig,axs = gen_pair_graphs(df, cols, title, xticks=range(time_in_oven+1))
    title = title.split('\n')
    figs[title[1]] = fig
    ## struc ##

    ## ΔΔholin-lysin ##
    title = f'Lysis Curve - {deg}°C\nΔΔholin-lysin'
    cols = wt_cols + [ c for c in df.columns if 'holin-lysin' in c ]
    fig,axs = gen_pair_graphs(df, cols, title, xticks=range(time_in_oven+1))
    title = title.split('\n')
    figs[title[1]] = fig
    ## Δ01555-56 ##


    # save dict
    for title,fig in figs.items():
        path = f'./figs/{output_folder}/{csv_filename}'
        os.makedirs(path, exist_ok=True)
        print(f'saving {title} figure..')
        fig.savefig(f'{path}/{title}.png')

    print('done')

    # show
    # plt.show()