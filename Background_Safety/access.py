from Utilities.functions import set_face

def deny_access():
    for i in range(1, 10):
        set_face("deny_1")
        time.sleep(1)
        set_face("deny_2")
        time.sleep(1)
