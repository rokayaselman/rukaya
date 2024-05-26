Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def is_binary(binary_str):
    for char in binary_str:
        if char not in('0','1'):
            return False
        return True
def bin_to_dec(binary_str):
    decnum=0
    binary_str=binary_str[::-1]
    for i in range(len(binary_str)):
        decnum+=int(binary_str[i])*(2**i)
    return decnum 
def main():
    while True:
        binary_str=input("ادخل رقم ثنائي:").strip()
        if is_binary(binary_str):
            decnum=bin_to_dec(binary_str)
            print("المكافئ العشري للرقم الثنائي",(binary_str),"هو",(decnum)(
            break
        else :
            print("خيار خطأ ,ادخل رقم ثنائي يحيوي فقط 0 او 1")
if __name__=="__main__" :
    main()

