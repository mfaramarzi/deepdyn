from mat_utils import Mat
import graph_utils as gt
import numpy as np
import image_utils as img

if __name__ == '__main__':

    file = Mat('wide_image_03.mat')

    image = file.get_image('I2')

    # img.show_image(image[:,:,1])
    # img.slide_and_construct(image[:, :, 1])

    auxiliary_graph = file.get_graph('A')
    node_pos = file.get_graph('V')

    veins_color = (gt.color_vein(v) for v in file.get_graph('art'))
    arteries_color = (gt.color_artery(a) for a in file.get_graph('ven'))

    color = (gt.color_av(a, v) for a, v in zip(file.get_graph('art'), file.get_graph('ven')))

    gt.show_graph(auxiliary_matrix=auxiliary_graph,node_pos=node_pos,node_color=''.join(color))
