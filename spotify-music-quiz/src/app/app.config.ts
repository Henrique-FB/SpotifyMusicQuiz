import { ApplicationConfig, importProvidersFrom } from '@angular/core';
import { provideRouter } from '@angular/router';
import { environment } from '../environments/environment';

import { routes } from './app.routes';
import { provideClientHydration } from '@angular/platform-browser';
import { SocketIoModule, SocketIoConfig } from 'ngx-socket-io';

const config: SocketIoConfig = { url: environment.apiBaseUrl, options: {} };

export const appConfig: ApplicationConfig = {
  providers: [
              provideRouter(routes), 
              provideClientHydration(), 
              importProvidersFrom(SocketIoModule.forRoot(config))
            ]
};
