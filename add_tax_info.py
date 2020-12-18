from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from create import Data

from selenium import webdriver




engine = create_engine('sqlite:///parcel.db', echo=True)

Session = sessionmaker(bind = engine)
session = Session()


driver = webdriver.Chrome()
        
for i in range(100):
    if (i==0):
        continue
    url = "https://www.gfxtra31.com/adobe-after-effects/page/"+str(i)+"/"
    driver.get(url)
    
    
    titles=driver.find_elements_by_xpath("//*[@id='mcontent_inner_box']//div[contains(@class, 'baslik')]//a")
    for title in titles:
        title_=title.text
        url_=title.get_attribute("href")
        c1 = Data(title = title_, url = url_)

        session.add(c1)
    session.commit()
        
     