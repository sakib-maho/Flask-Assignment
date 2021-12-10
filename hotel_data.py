import mysql.connector
import json




mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="My_hotel"
)


# SELECT *
# FROM customers
# WHERE (state = 'California' AND last_name = 'Johnson')
# OR (customer_id > 4500);


def location(city, price, length, bedrooms, bathrooms, sleeps, title):

  jsonData = []
  # city = 'Panama'

  mycursor = mydb.cursor()
  sql = ''
  # if length == 1:
  #   sql = ("SELECT * FROM Hotel_data WHERE (Location =" + f"'{city}' OR Price=" + f"'${price}')")
  # elif length == 2:
  #   print("hello")
  #   sql = ("SELECT * FROM Hotel_data WHERE Bedrooms = '3 Bedrooms'")

  sql = "SELECT * FROM Hotel_data WHERE"



  city_e = True
  price_e = True
  bedrooms_e = True
  bathrooms_e = True
  title_e = True
  sleeps_e = True


  if city != None:
    sql = sql + " Location=" + f"'{city}'"
    city_e = False

  elif price != None:
    sql = sql + " Price>= " + f'{price}'
    price_e = False

  elif bedrooms != None:
    sql = sql + " Bedrooms>=" + f"'{bedrooms}'"
    bedrooms_e = False

  elif bathrooms != None:
    sql = sql + " Bathrooms>=" + f"'{bathrooms}'"
    bathrooms_e = False

  elif title != None:
    sql = sql + " Title =" + f"'{title}'"
    title_e = False

  elif sleeps != None:
    sql = sql + " Sleeps >=" + f"'{sleeps}'"
    sleeps_e = False

  for i in range(length):
    if 1 < i + 1 < length+1:
      if city != None and city_e:
        sql = sql + 'AND'
        sql = sql + " Location =" + f"'{city}'"
        city_e = False

      if price != None and price_e:
        sql = sql + 'AND'
        sql = sql + " Price>=" + f'{price}'
        price_e = False

      if bedrooms != None and bedrooms_e:
        sql = sql + 'AND'
        sql = sql + " Bedrooms >=" + f"'{bedrooms}'"
        bedrooms_e = False

      if bathrooms != None and bathrooms_e:
        sql = sql + 'AND'
        sql = sql + " Bathrooms >=" + f"'{bathrooms}'"
        bathrooms_e = False

      if title != None and title_e:
        sql = sql + 'AND'
        sql = sql + " Title =" + f"'{title}'"
        title_e = False

      if sleeps is not None and sleeps_e:
        sql = sql + 'AND'
        sql = sql + " Sleeps >=" + f"'{sleeps}'"
        sleeps_e = False

  #
  #
  # sql = sql + " Location =" + f"'{city}'" + 'AND' + " Price =" + f"'{price}'"
  # if city != ',' and price != ',':
  #   sql = ("SELECT * FROM Hotel_data WHERE (Location =" + f"'{city}' AND Price=" + f"'{price}')")


  print(sql)
  mycursor.execute(sql)

  myresult = mycursor.fetchall()

  for x in myresult:
    data = {
      "Title": x[0],
      "Sleeps": x[1],
      "Bedrooms": x[2],
      "Bathrooms": x[3],
      "Price": x[4],
      "Pictures": {
        "Picture_1": x[5],
        "Picture_2": x[6],
        "Picture_3": x[7],
      },
      "Location": x[8],
    }
    jsonData.append(data)

  sorted_list = sorted(jsonData, key=lambda k: int(k["Price"]))
  json_object = json.dumps(sorted_list, indent = 4)
  print(json_object)
  return json_object
