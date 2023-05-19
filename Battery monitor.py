{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "416ffff0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import psutil\n",
    "from plyer import notification\n",
    "\n",
    "def battery_notification():\n",
    "    battery = psutil.sensors_battery()\n",
    "    plugged = battery.power_plugged\n",
    "    percent = battery.percent\n",
    "\n",
    "    if plugged:\n",
    "        if percent >= 100:\n",
    "            notification.notify(\n",
    "                title=\"Battery Status\",\n",
    "                message=\"Battery is fully charged. Please unplug the charger.\",\n",
    "                timeout=10\n",
    "            )\n",
    "    else:\n",
    "        if percent <= 20:\n",
    "            notification.notify(\n",
    "                title=\"Battery Status\",\n",
    "                message=\"Battery is below 20%. Please connect the charger.\",\n",
    "                timeout=10\n",
    "            )\n",
    "\n",
    "def main():\n",
    "    while True:\n",
    "        battery_notification()\n",
    "        # Check battery status every 60 seconds\n",
    "        psutil.wait_services(timeout=60)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    main()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
