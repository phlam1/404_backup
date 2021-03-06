/**
 * API Git static class
 */
export default class ApiGit {
    static handleErrors(response) {
        if (!response.ok) {
            console.log("error", response);
            throw new Error(response.statusText);
        }
        return response.json();
    };

    static getEvents(action) {
        let response = [];

        console.log('GitAPI');
        return fetch('https://api.github.com/users/' + action.username + '/events', {
            method: 'GET'
        }).then((response) => {
            return ApiGit.handleErrors(response);
        }).then((response) => {
            return {
                response
			};
        });
    }

    static getUser(action) {
        let response = [];

        console.log('GitAPI');
        return fetch('https://api.github.com/users/' + action.username, {
            method: 'GET'
        }).then((response) => {
            return ApiGit.handleErrors(response);
        }).then((response) => {
            return {
                response
            };
        });
    }
}
