#!/usr/bin/env python

import requests


class Cachet(object):
    def __init__(self, url, apiToken):
        self.url = url
        self.apiToken = apiToken

    def __getRequest(self, path):
        return requests.get(self.url + path, headers={'X-Cachet-Token': self.apiToken})

    def __postRequest(self, path, data):
        return requests.post(self.url + path, data, headers={'X-Cachet-Token': self.apiToken})

    def __putRequest(self, path, data):
        return requests.put(self.url + path, data, headers={'X-Cachet-Token': self.apiToken})

    def __delRequest(self, path):
        return requests.delete(self.url + path, headers={'X-Cachet-Token': self.apiToken})

    def ping(self):
        return self.__getRequest('/ping')

    def getComponents(self):
        return self.__getRequest('/components')

    def getComponentsByID(self, id):
        return self.__getRequest('/components/%s' % id)

    def postComponents(self, name, status, **kwargs):
        kwargs['name'] = name
        kwargs['status'] = status
        return self.__postRequest('/components', kwargs)

    def putComponentsByID(self, id, **kwargs):
        return self.__putRequest('/components/%s' % id, kwargs)

    def deleteComponentsByID(self, id):
        return self.__delRequest('/components/%s' % id)

    def getComponentsGroups(self):
        return self.__getRequest('/components/groups')

    def getComponentsGroupsByID(self, id):
        return self.__getRequest('/components/groups/%s' % id)

    def postComponentsGroups(self, name, **kwargs):
        kwargs['name'] = name
        return self.__postRequest('/components/groups', kwargs)

    def putComponentsGroupsByID(self, id, **kwargs):
        return self.__putRequest('/components/groups/%s' % id, kwargs)

    def deleteComponentsGroupsByID(self, id):
        return self.__getRequest('/components/groups/%s' % id)

    def getIncidents(self):
        return self.__getRequest('/incidents')

    def getIncidentsByID(self, id):
        return self.__getRequest('/incidents/%s' % id)

    def postIncidents(self, name, message, status, visible, **kwargs):
        kwargs['name'] = name
        kwargs['message'] = message
        kwargs['status'] = status
        kwargs['visible'] = visible
        return self.__postRequest('/incidents', kwargs)

    def putIncidentsByID(self, id, **kwargs):
        return self.__putRequest('/incidents/%s' % id, kwargs)

    def deleteIncidentsByID(self, id):
        return self.__delRequest('/incidents/%s' % id)

    def getMetrics(self):
        return self.__getRequest('/metrics')

    def postMetrics(self, name, suffix, description, default_value, **kwargs):
        kwargs['name'] = name
        kwargs['suffix'] = suffix
        kwargs['description'] = description
        kwargs['default_value'] = default_value
        return self.__postRequest('/metrics', kwargs)

    def getMetricsByID(self, id):
        return self.__getRequest('/metrics/%s' % id)

    def deleteMetricsByID(self, id):
        return self.__delRequest('/metrics/%s' % id)

    def getMetricsPointsByID(self, id):
        return self.__getRequest('/metrics/%s/points' % id)

    def postMetricsPointsByID(self, id, value, **kwargs):
        kwargs['value'] = value
        return self.__postRequest('/metrics/%s/points' % id, kwargs)

    def deleteMetricsPointsByID(self, id):
        return self.__delRequest('/metrics/%s/points' % id)

    def getSubscribers(self):
        return self.__getRequest('/subscribers')

    def postSubscribers(self, email, **kwargs):
        kwargs['email'] = email
        return self.__postRequest('/subscribers', kwargs)

    def deleteSubscribersByID(self, id):
        return self.__delRequest('/subscribers/%s' % id)
