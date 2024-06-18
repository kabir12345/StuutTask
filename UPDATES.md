## Possible Improvemnets
- Better implementation of CSS on elements like the search bar, bottons and the table
- Collapsable table for the ability to show and hide information as needed
- Ability to compare stocks side by side.
- Ability to use chart.js to utilize the history method of yfinance's library to chart the stocks momvemnet in real time.

## To take this project to production
- we can containerise the application using Dockers to deploy on our server. Use Kubernetes to auto scale when requiremnts surge or downgrades.
- provide and API end point for other developers to request the data easily.

## Notes
- Had to change the API port to 5005 since another service was occupying my port 5000