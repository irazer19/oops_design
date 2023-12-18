# Create observers
from observer import EmailAlertObserver
from observable import IphoneObservable

iphone = IphoneObservable()

saurav = EmailAlertObserver(
    username="Saurav", email="irazer19@gmail.com", observable=iphone
)

iphone.add(saurav)
iphone.set_data(stock_count=10)
