import { SpotifyApi } from '@spotify/web-api-ts-sdk';
import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';

@Injectable({
    providedIn: 'root',
})

export class SpotifyService {
  
    sdk: SpotifyApi = SpotifyApi.withClientCredentials(environment.spotifyClient, environment.spotifySecret, ["user-read-private"]);
    
    constructor() {}
}

