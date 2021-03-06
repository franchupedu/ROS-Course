#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/franchupedu/hrwros_ws/src/hrwros_factory_behaviors/behaviors/behavior_final_project"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/franchupedu/hrwros_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/franchupedu/hrwros_ws/install/lib/python2.7/dist-packages:/home/franchupedu/hrwros_ws/build/behavior_final_project/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/franchupedu/hrwros_ws/build/behavior_final_project" \
    "/usr/bin/python2" \
    "/home/franchupedu/hrwros_ws/src/hrwros_factory_behaviors/behaviors/behavior_final_project/setup.py" \
    build --build-base "/home/franchupedu/hrwros_ws/build/behavior_final_project" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/franchupedu/hrwros_ws/install" --install-scripts="/home/franchupedu/hrwros_ws/install/bin"
