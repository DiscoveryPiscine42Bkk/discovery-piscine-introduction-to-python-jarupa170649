import sys #runโดยใช้ python3 count_it.py

args = sys.argv[1:]

if len(args) == 0:
    print("none")
else:
    print(f"parameters: {len(args)}")
    for arg in args:
        print(f"{arg}: {len(arg)}")
/workspaces/discovery-piscine-introduction-to-python-jarupa170649/cell05/ex11