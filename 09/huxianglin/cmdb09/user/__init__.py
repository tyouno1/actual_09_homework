#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
import os
app=Flask(__name__)
app.secret_key = os.urandom(32)
import views