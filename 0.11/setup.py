#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name = 'PlannedMilestones',
    version = '0.1',
    packages = ['plannedmilestones'],

    author = "Jørn A Hansen",
    description = "The PlannedMilestonesMacro displays a bulleted list of milestones ordered by their due dates. ",
    license = "GPL",
    keywords = "trac milestones plugin",
    url = "http://trac-hacks.org/wiki/PlannedMilestonesMacro",
    classifiers = [
        'Framework :: Trac',
    ],
    

    entry_points = {
        'trac.plugins': [
            'plannedmilestones.PlannedMilestones = plannedmilestones.PlannedMilestones',
        ]
    }
)

