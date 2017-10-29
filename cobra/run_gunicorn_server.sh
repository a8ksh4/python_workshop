#!/bin/sh
if which gunicorn3; then
    gunicorn3 cobra_server:app
else
    gunicorn cobra_server:app
fi
