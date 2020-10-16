# Auth0 Proof of Concept

## Tasks
- [X] Set up frontent
- [ ] Set up backend
- [ ] Frontend:
	- [X] Initialize repository
	- [X] Add in basic Auth0 authentication
	- [X] Add in authentication so only `@fuseinsurance.ca` addresses can log in
	- [X] Add routes that can be accessed whether authenticated or not
	- [X] Add routes that can only be accessed when authenticated
	- [X] Explicitly get and store the authentication token
	- [ ] Make unsecured API calls
	- [ ] Make secured API calls
- [ ] Backend:
	- [X] Basic setup
	- [ ] Create graphql route
	- [ ] Accept and return unverified requests
	- [ ] Accept JWTs from the frontend
	- [ ] Verify them:
		- [ ] Issuer
		- [ ] Expiry
	- [ ] Accept and return a verified API call
- [ ] ??? Refresh Tokens ??? 
	  -[ ] Somehow deal with refresh tokens, if necessary - we can keep people logged for >24 hours, so do we even need this?
