var portfolioApp = angular.module('portfolioApp', []);

portfolioApp.controller('GalleryListCtrl', function($scope) {
    $scope.galleries = [
        {
            'title': 'Jemen',
            'when': '2017-01-05',
            'thumbnailUrl': 'img/podroz1.jpg'
        },
        {
            'title': 'USA',
            'when': '2012-02-10',
            'thumbnailUrl': 'img/podroz2.jpg'
        },
        {
            'title': 'Estonia',
            'when': '2011-05-24',
            'thumbnailUrl': 'img/podroz3.jpg'
        },
        {
            'title': 'Niemcy',
            'when': '2018-06-12',
            'thumbnailUrl': 'img/podroz4.jpg'
        },
        {
            'title': 'Litwa',
            'when': '2010-03-09',
            'thumbnailUrl': 'img/podroz5.jpg'
        },
        {
            'title': 'Polska',
            'when': '2017-12-07',
            'thumbnailUrl': 'img/podroz6.jpg'
        }
    ];
    $scope.sortList = [
        {
            'label':'Alfabetycznie',
            'value':'title'
        },
        {
            'label':'Chronologicznie',
            'value':'when'
        },
        {
            'label':'Od najnowszych',
            'value':'-when'
        },
    ];
});