#!/bin/sh
echo $USER
echo "ps :" 
ps
echo "Appuyez sur une touche pour continuer"
read
echo "mon ps :" 
ps.py 

echo "Appuyez sur une touche pour continuer"
read
echo "ps -a :" 
ps -a
echo "Appuyez sur une touche pour continuer"
read
echo "mon ps -a :" 
ps.py -a

echo "Appuyez sur une touche pour continuer"
read
echo "ps -x :" 
ps -x
echo "Appuyez sur une touche pour continuer"
read
echo "mon ps -x :" 
ps.py -x

echo "Appuyez sur une touche pour continuer"
read
echo "ps -u :" 
ps -u
echo "Appuyez sur une touche pour continuer"
read
echo "mon ps -u :" 
ps.py -u

echo "Appuyez sur une touche pour continuer"
read
echo "ps -u $USER :" 
ps -u $USER
echo "Appuyez sur une touche pour continuer"
read
echo "mon ps -u $USER :" 
ps.py -u $USER


