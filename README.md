# Supertokens Python SDK "No Supertokens Core available to query" Reproduction Steps

Requirements:

- Docker
- [Bruno](https://usebruno.com)

1. Clone repo
2. Run `./run_dev.sh`
3. Open Bruno and load the collection in `bruno/Test`
4. Try the "Test Hello" endpoint to confirm the server is running
5. Try the "Sign up" endpoint. In most cases, it will fail with the error "No Supertokens Core available to query".
6. If it fails, try the "Sign up" endpoint again. It should work this time.
7. Change the `/` endpoint response to "Hello World 2", save the file. The dev server should restart.
8. Try the "Sign in" endpoint. It should fail with the error "No Supertokens Core available to query".
9. Try the "Sign in" endpoint again. It should work this time.
