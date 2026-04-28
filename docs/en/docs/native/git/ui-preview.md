---
hide:
  - toc
---

# Frontend UI Translation Preview

After translating the frontend UI, you can preview the real-time effect locally. For example, adjust word length, case, check consistency, etc.

1. Enter the repo root directory and create __.env.local__ local environment file.

    ```shell
    touch .env.local
    ```

2. Set local environment variables.

    ```shell
    cat <<EOF > .env.local
    VUE_APP_API_URL=http://demo-dev.daocloud.io
    VUE_APP_AUTH=eyJhbGciOiJSUzI1NiIsImtpZCI6IkRKVjlBTHRBLXZ4MmtQUC1TQnVGS0dCSWc1cnBfdkxiQVVqM2U3RVByWnMiLCJ0eXAiOiJKV1QifQ.eyJpYXQiOjE2ODUzNTY0NDMsImlzcyI6ImdoaXBwby5pbyIsInN1YiI6IjQzODIxMmI3LTFhNDYtNDE4Ny04ODI0LTYwZWE5ZDBkOTNiMyIsInByZWZlcnJlZF91c2VybmFtZSI6ImFkbWluIiwiZ3JvdXBzIjpbXSwiaWQiOiJmOWY3NmU5NC1mYjRjLTRlMGUtYmZlYy0wNmIwYmE0MzM0OWYifQ.dSQFtEIqe520ZMaT82vcQ8Y6YmIbWqz4SZPLHxJcjpCrHBg_Ke1asEymyz3AJC9WkF30JR7Eqpfmgt6Gc05op7Tt12-QG527fbW8pWQjZhWx8-u2ev6MZtCQQjoAA4w03MozUfiEI-VFdoI0in2MBi2bdKBVGRpeW2DwCQyN6jR5F-ZKm4ObP8dD7WnfcjsVSrLHBBJ1jeU9d1qAVNc1IxXSyG2p2FrIXa4_ds5Al_8l38NJ4LuyeVnoefzP6dDpemTGzavwfDtmXdATMV5jqHADji1Zbe-5YyV-3SwQCiN7XQmLCht4NpqA3NRYC1Tv134wrzsBvfB0HVIwAjgrpA
    EOF
    ```

3. Install dependencies.

    ```shell
    npm install
    ```
