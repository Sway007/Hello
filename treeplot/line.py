__author__ = 'Sway007'

import matplotlib.pyplot as plt


def nodePlot(p, pStr, axis):

    axis.text(p[0], p[1], pStr,
              bbox=dict(facecolor='black', alpha=0.5),
              ha='center',
              va='center'
              )

def linePlot(head, headStr, nodePointed, pointedStr, axis):
    '''

    :param head: tuple:(x, y)
    :param nodePointed:
    :return: None
    '''

    # plot arrow
    axis.annotate('', xy=nodePointed, xytext=head,
                  xycoords='data',
                  textcoords='data',
                  arrowprops=dict(facecolor='red', shrink=0.2,
                                  width=1.0, lw=1.0),
                  ha='center',
                  va='center',
                  )

    # plot nodes
    nodePlot(head, headStr, axis)
    nodePlot(nodePointed, pointedStr, axis)

def main():
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # test codes
    linePlot((0.1, 0.1), 'Head', (0.3, 0.3), 'Tail', ax)

    plt.show()


if __name__ == '__main__':
    main()