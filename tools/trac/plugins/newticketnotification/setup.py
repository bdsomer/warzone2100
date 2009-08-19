#!/usr/bin/env python
# vim: set et sts=4 sw=4 encoding=utf8:
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name = 'NewTicketNotification',
    version = '0.1',

    packages = ['newticketnotification'],
    package_data = { 'newticketnotification': ['templates/*.html'] },

    install_requires = ['trac>=0.11'],

    author = 'Giel van Schijndel',
    author_email = 'me@mortis.eu',
    description = 'Extends Trac to notify a configured set of e-mail addresses upon ticket creation.',
    license = 'BSD',
    keywords = 'trac plugin ticket create notify e-mail',
    url = 'http://developer.wz2100.net/browser/trunk/tools/trac/plugins/newticketnotification',
    classifiers = [
        'Framework :: Trac',
        'License :: OSI Approved :: BSD License',
    ],

    entry_points = {
        'trac.plugins': [
            'newticketnotification.admin = newticketnotification.admin',
            'newticketnotification.main = newticketnotification.main',
        ],
    },
)
