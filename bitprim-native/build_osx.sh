# ARCHFLAGS="-arch i386 -arch x86_64" python setup.py build
# ARCHFLAGS="-arch i386 -arch x86_64" pip install  -v -e .

echo $ARCHFLAGS
echo $LDSHARED

# export LDSHARED="cc -bundle -Wl,-F. -arch x86_64"
export ARCHFLAGS="-arch x86_64" 

echo $ARCHFLAGS
echo $LDSHARED

./reset.sh
pip install  -v -e .

#sudo pip install  -v -e .
