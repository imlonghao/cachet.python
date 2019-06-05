#!/usr/bin/env python

import requests


class Cachet(object):
    def __init__(self, url, apiToken):
        self.url = url
        self.apiToken = apiToken

    def __getRequest(self, path, params=None):
        return requests.get(self.url + path, params=params, headers={'X-Cachet-Token': self.apiToken})

    def __postRequest(self, path, data):
        return requests.post(self.url + path, data, headers={'X-Cachet-Token': self.apiToken})

    def __putRequest(self, path, data):
        return requests.put(self.url + path, data, headers={'X-Cachet-Token': self.apiToken})

    def __delRequest(self, path):
        return requests.delete(self.url + path, headers={'X-Cachet-Token': self.apiToken})

    def ping(self):
        '''API test endpoint.

        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__getRequest('/ping')

    def getComponents(self):
        '''Return all components that have been created.

        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__getRequest('/components')

    def searchComponents(self, id=None, name=None, status=None, group_id=None, enabled=None, sort=None, order='desc', per_page=None):
        '''
        Search for Components using the advance api usage.

        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''
        params={}
        params['id']=id
        params['name']=name
        params['status']=status
        params['group_id']=group_id
        params['enabled']=enabled
        params['sort']=sort
        params['order']=order
        params['per_page']=per_page
        
        return self.__getRequest('/components', params=params)

    def getComponentsByID(self, id):
        '''Return a single component.

        :param id: Component ID
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__getRequest('/components/%s' % id)

    def postComponents(self, name, status, **kwargs):
        '''Create a new component.

        :param name: Name of the component
        :param status: Status of the component; 1-4
        :param description: (optional) Description of the component
        :param link: (optional) A hyperlink to the component
        :param order: (optional) Order of the component
        :param group_id: (optional) The group id that the component is within
        :param enabled: (optional)
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        kwargs['name'] = name
        kwargs['status'] = status
        return self.__postRequest('/components', kwargs)

    def putComponentsByID(self, id, **kwargs):
        '''Updates a component.

        :param id: Component ID
        :param name: (optional) Name of the component
        :param status: (optional) Status of the component; 1-4
        :param link: (optional) A hyperlink to the component
        :param order: (optional) Order of the component
        :param group_id: (optional) The group id that the component is within
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__putRequest('/components/%s' % id, kwargs)

    def deleteComponentsByID(self, id):
        '''Delete a component.

        :param id: Component ID
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__delRequest('/components/%s' % id)

    def getComponentsGroups(self):
        '''

        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__getRequest('/components/groups')

    def searchComponentsGroups(self, id=None, name=None, collapsed=None, visible=None, sort=None, order='desc', per_page=None):
        '''
        Search for ComponentsGroups using the advance api usage.

        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''
        params={}
        params['id']=id
        params['name']=name
        params['collapsed']=collapsed
        params['visible']=visible
        params['sort']=sort
        params['order']=order
        params['per_page']=per_page

        return self.__getRequest('/components/groups', params=params)

    def getComponentsGroupsByID(self, id):
        '''

        :param id: ID of the group you want to fetch
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__getRequest('/components/groups/%s' % id)

    def postComponentsGroups(self, name, **kwargs):
        '''

        :param name: Name of the component group
        :param order: (optional) Order of the component group
        :param collapsed: (optional) Whether to collapse the group by default
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        kwargs['name'] = name
        return self.__postRequest('/components/groups', kwargs)

    def putComponentsGroupsByID(self, id, **kwargs):
        '''

        :param id: Component group to update
        :param name: (optional) Name of the component group
        :param order: (optional) Order of the group
        :param collapsed: (optional) Whether to collapse the group by default
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__putRequest('/components/groups/%s' % id, kwargs)

    def deleteComponentsGroupsByID(self, id):
        '''

        :param id: Component group to delete
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__getRequest('/components/groups/%s' % id)

    def getIncidents(self):
        '''Return all incidents.

        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__getRequest('/incidents')

    def searchIncidents(self, id=None, component_id=None, name=None, status=None, visible=None, sort=None, order='desc', per_page=None):
        '''
        Search for Incidents using the advance api usage.

        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''
        
        params={}
        params['id']=id
        params['component_id']=component_id
        params['name']=name
        params['status']=status
        params['visible']=visible
        params['sort']=sort
        params['order']=order
        params['per_page']=per_page
        
        return self.__getRequest( '/incidents', params=params)
    
    def getIncidentsByID(self, id):
        '''Returns a single incident.

        :param id: Incident ID
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__getRequest('/incidents/%s' % id)

    def postIncidents(self, name, message, status, visible, **kwargs):
        '''Create a new incident.

        :param name: Name of the incident
        :param message: A message (supporting Markdown) to explain more.
        :param status: Status of the incident.
        :param visible: Whether the incident is publicly visible.
        :param component_id: (optional) Component to update.
        :param component_status: (optional) The status to update the given component with.
        :param notify: (optional) Whether to notify subscribers.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        kwargs['name'] = name
        kwargs['message'] = message
        kwargs['status'] = status
        kwargs['visible'] = visible
        return self.__postRequest('/incidents', kwargs)

    def putIncidentsByID(self, id, **kwargs):
        '''

        :param id: ID of the incident to update.
        :param name: (optional) Name of the incident
        :param message: (optional) A message (supporting Markdown) to explain more.
        :param status: (optional) Status of the incident.
        :param visible: (optional) Whether the incident is publicly visible.
        :param component_id: (optional) Component to update.
        :param notify: (optional) Whether to notify subscribers.
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__putRequest('/incidents/%s' % id, kwargs)

    def deleteIncidentsByID(self, id):
        '''Delete an incident.

        :param id: Incident ID
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__delRequest('/incidents/%s' % id)

    def getMetrics(self):
        '''Returns all metrics that have been setup.

        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__getRequest('/metrics')

    def postMetrics(self, name, suffix, description, default_value, **kwargs):
        '''Create a new metric.

        :param name: Name of metric
        :param suffix: Measurments in
        :param description: Description of what the metric is measuring
        :param default_value: The default value to use when a point is added
        :param display_chart: (optional) Whether to display the chart on the status page
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        kwargs['name'] = name
        kwargs['suffix'] = suffix
        kwargs['description'] = description
        kwargs['default_value'] = default_value
        return self.__postRequest('/metrics', kwargs)

    def getMetricsByID(self, id):
        '''Returns a single metric, without points.

        :param id: Metric ID
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__getRequest('/metrics/%s' % id)

    def deleteMetricsByID(self, id):
        '''Delete a metric.

        :param id: Metric ID
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__delRequest('/metrics/%s' % id)

    def getMetricsPointsByID(self, id):
        '''Return a list of metric points.

        :param id: Metric ID
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__getRequest('/metrics/%s/points' % id)

    def postMetricsPointsByID(self, id, value, **kwargs):
        '''Add a metric point to a given metric.

        :param id: Metric ID
        :param value: Value to plot on the metric graph
        :param timestamp: Unix timestamp of the point was measured
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        kwargs['value'] = value
        return self.__postRequest('/metrics/%s/points' % id, kwargs)

    def deleteMetricsPointsByID(self, id, point_id):
        '''Delete a metric point.

        :param id: Metric ID
        :param point_id: Metric Point ID
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__delRequest('/metrics/%s/points/%s' % (id, point_id))

    def getSubscribers(self):
        '''Returns all subscribers.

        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__getRequest('/subscribers')

    def postSubscribers(self, email, **kwargs):
        '''Create a new subscriber.

        :param email: Email address to subscribe
        :param verify: (optional) Whether to send verification email
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        kwargs['email'] = email
        return self.__postRequest('/subscribers', kwargs)

    def deleteSubscribersByID(self, id):
        '''Delete a subscriber.

        :param id: ID of the subscriber to delete
        :return: :class:`Response <Response>` object
        :rtype: requests.Response
        '''

        return self.__delRequest('/subscribers/%s' % id)
