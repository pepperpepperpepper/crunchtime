sudo apt-get install libjack-jack2-dev libportmidi-dev portaudio19-dev liblo-dev
sudo apt-get install libsndfile-dev python-dev python-tk subversion
sudo apt-get install python-imaging-tk python-wxgtk2.8
svn checkout http://pyo.googlecode.com/svn/trunk/ pyo-read-only
cd pyo-read-only
sudo python setup.py install --install-layout=deb --use-jack --use-double

