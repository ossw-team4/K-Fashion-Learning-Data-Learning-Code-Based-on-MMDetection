import os

path_dir = './data/clothes'
dir_list = os.listdir(path_dir)

def replace_str(file_path, old_str, new_str):
    fr = open(file_path, 'r')
    lines = fr.readlines()
    fr.close()
    
    fw = open(file_path, 'w')
    for line in lines:
        fw.write(line.replace(old_str, new_str))
    fw.close()
 
tmp_path = [
    "/tmp/tmput84ebrk/images/", "/tmp/tmp0mjsxlac/images/", "/tmp/tmp9ge37aoo/images/",
    "/tmp/tmp0dp5v68v/images/", "/tmp/tmpmp7cnwm8/images/", "/tmp/tmpoo4iyx5_/images/",
    "/tmp/tmpyru93_mf/images/", "/tmp/tmp0om7sr_m/images/", "/tmp/tmpflunb2lq/images/",
    "/tmp/tmpu60k5s6v/images/", "/tmp/tmpgm1nh21k/images/", "/tmp/tmp2uk309o_/images/",
    "/tmp/tmpoyhe7bfj/images/", "/tmp/tmpnes9_5ph/images/", "/tmp/tmpki5vbp80/images/",
    "/tmp/tmp4fa3uanv/images/", "/tmp/tmphcmezoks/images/", "/tmp/tmp133olbqd/images/",
    "/tmp/tmp46ug0znj/images/", "/tmp/tmpu1cfv3_6/images/", "/tmp/tmpb3ws57vl/images/",
    "/tmp/tmp0xoja8ql/images/", "/tmp/tmplrrxa3p0/images/", "/tmp/tmpytyvnyyf/images/",
    "/tmp/tmpjpe3hvpb/images/"
]

i = 0
for dir in dir_list:
    if dir[-4:] == ".zip":
        continue
    if dir=="remove_tmp.py":
        continue
    file_path = path_dir + "/" + str(dir) + "/annotations/instances_default.json"
    replace_str(file_path, tmp_path[i], "")
    i = i + 1