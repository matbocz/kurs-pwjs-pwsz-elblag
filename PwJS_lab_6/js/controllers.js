var portfolioApp = angular.module('portfolioApp', []);

portfolioApp.controller('GalleryListCtrl', function($scope) {
    $scope.galleries = [
        {
            'title': 'Podróż 1',
            'when': '2014-01-05',
            'thumbnailUrl': 'img/podroz1.jpg'
        },
        {
            'title': 'Podróż 2',
            'when': '2014-02-10',
            'thumbnailUrl': 'img/podroz2.jpg'
        },
        {
            'title': 'Podróż 3',
            'when': '2015-05-24',
            'thumbnailUrl': 'img/podroz3.jpg'
        },
        {
            'title': 'Podróż 4',
            'when': '2015-06-12',
            'thumbnailUrl': 'img/podroz4.jpg'
        },
        {
            'title': 'Podróż 5',
            'when': '2016-03-09',
            'thumbnailUrl': 'img/podroz5.jpg'
        },
        {
            'title': 'Podróż 6',
            'when': '2017-12-07',
            'thumbnailUrl': 'img/podroz6.jpg'
        }
    ];
    $scope.galleries.length;
});