from cv2 import cv2
import pytesseract
import psycopg2
import re

#img=cv2.imread("/home/deadman/Videos/a.jpg")
#text=pytesseract.image_to_string(img)

#print(text)

def test():
    f=open('/home/deadman/Videos/customer_data.csv','r')
    content=f.read()
    print(content)
    try:
        conn=psycopg2.connect(host="localhost",database="awesome",user="postgres")
        cur=conn.cursor()
        #cur.execute("copy customer_info(f_name,l_name,vechile_no) from '/home/deadman/Videos/customer_data.csv' delimiter ',' csv header;") 
        
        #with open('/home/deadman/Videos/customer_data.csv','r') as g:
         #   for i in range(0,5):
          #      reader = g.read()
           #     cur.execute("insert into customer_info value (%s,%s,%s)".)
        
        #a=str(input("Enter vechile number = "))
        img=cv2.imread("/home/deadman/Pictures/a2.png")
        text=pytesseract.image_to_string(img)
        a3=str(text)
        a4=re.sub(r'[^\w]', ' ',a3).strip()
        print(a4)
        cur.execute(f"select * from customer_info where vechile_no = '{a4}';")
        print(f"NUmber of Records = {cur.rowcount}")
        row = cur.fetchall()
        print(row)
        
        # while row is not None:
            
        #     row = cur.fetchone()
        #     print(row)

        cur.close()
        #conn.commit()
    except (Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("connection closed")

if __name__=="__main__":
    test()
