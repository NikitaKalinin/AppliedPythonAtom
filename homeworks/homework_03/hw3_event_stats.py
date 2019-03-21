#!/usr/bin/env python
# coding: utf-8

import collections


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        # TODO: реализовать метод
        self.users_activity = {}

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        # TODO: реализовать метод
        if user_id not in self.users_activity:
            self.users_activity[user_id] = [time]
        else:
            self.users_activity[user_id].append(time)

    def query(self, count, time):
        """
        Этот метод отвечает на запросы.
        Возвращает количество пользователей, которые за последние 5 минут
        (на полуинтервале времени (time - 5 min, time]), совершили ровно count действий
        :param count: количество действий
        :param time: время для рассчета интервала
        :return: activity_count: int
        """
        # TODO: реализовать метод
        out = 0
        for user in self.users_activity:
            c = 0
            for active in self.users_activity[user]:
                if (time - 300) < active <= time:
                    c += 1
            if c == count and self.users_activity[user][0] < time:
                out += 1
        return out
