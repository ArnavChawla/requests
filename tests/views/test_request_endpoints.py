from urls import requests_url


def test_get_requests_succeeds(valid_request_model, client, request_headers):
    """
    Tests that response is okay.

    Args:
        valid_request_model (Model): a valid model created by a fixture.
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """
    res = client.get(requests_url(), headers=request_headers)
    response = res.get_json()

    assert response['success']
    assert response['message'] == 'requests fetched successfully'
    assert len(response['data']) == 1
    assert res.status_code == 200


def test_get_request_succeeds_with_valid_request_id_in_params(
    valid_request_model, client, request_headers
):
    """
    Tests that response is okay when request id exists.

    Args:
        valid_request_model (Model): a valid model created by a fixture.
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """
    res = client.get(requests_url(1), headers=request_headers)
    response = res.get_json()

    assert response['success']
    assert response['message'] == 'request fetched successfully'
    assert response['data']['title'] == 'Improve customer care services'
    assert res.status_code == 200


def test_get_request_succeeds_with_non_existent_request_id_in_params(
    client, request_headers
):
    """
    Tests that response is okay when request id exists.

    Args:
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """
    res = client.get(requests_url(1), headers=request_headers)
    response = res.get_json()

    assert not response['success']
    assert response['message'] == 'cannot find specified request'
    assert res.status_code == 404


def test_post_requests_succeeds_with_valid_request_body(
    valid_request_body, client, request_headers
):
    """
    Tests that response is okay when request body is valid.

    Args:
        valid_request_body (dict): a valid request body created by a fixture.
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """
    res = client.post(
        requests_url(), headers=request_headers, json=valid_request_body
    )
    response = res.get_json()

    assert response['success']
    assert response['message'] == 'request created successfully'
    assert response['data']['title'] == 'Improve customer care services'
    assert res.status_code == 201


def test_post_requests_succeeds_with_existing_priority_in_body(
    valid_request_body_with_existing_priority, client, request_headers
):
    """
    Tests that response shows failure when request body has conflicting
    priority.

    Args:
        valid_request_body_with_existing_priority (dict): a request body
            with existing priority for a client
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """
    res = client.post(
        requests_url(),
        headers=request_headers,
        json=valid_request_body_with_existing_priority
    )
    response = res.get_json()

    assert response['success']
    assert (response['message'] == 'request created successfully')
    assert res.status_code == 201


def test_post_requests_fails_with_missing_fields_in_request_body(
    invalid_request_body_with_missing_fields, client, request_headers
):
    """
    Tests that response shows failure when request body has missing fields.

    Args:
        invalid_request_body_with_missing_fields (dict): a request body with
            missing fields created by a fixture.
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """
    res = client.post(
        requests_url(),
        headers=request_headers,
        json=invalid_request_body_with_missing_fields
    )
    response = res.get_json()

    assert not response['success']
    assert (
        response['message']['client_id'][0] ==
        'Missing data for required field.'
    )
    assert (
        response['message']['staff_id'][0] ==
        'Missing data for required field.'
    )
    assert res.status_code == 400


def test_post_requests_fails_with_non_existent_client_in_body(
    invalid_request_body_with_non_existent_client, client, request_headers
):
    """
    Tests that response shows failure when request body has non-existent
    client id.

    Args:
        invalid_request_body_with_non_existent_client (dict): a request body
            with non-existent client id
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """
    res = client.post(
        requests_url(),
        headers=request_headers,
        json=invalid_request_body_with_non_existent_client
    )
    response = res.get_json()

    assert not response['success']
    assert response['message'] == 'cannot find specified client'
    assert res.status_code == 404


def test_post_requests_fails_with_non_existent_staff_in_body(
    invalid_request_body_with_non_existent_staff, client, request_headers
):
    """
    Tests that response shows failure when request body has non-existent
    staff id.

    Args:
        invalid_request_body_with_non_existent_staff (dict): a request body
            with non-existent staff id
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """
    res = client.post(
        requests_url(),
        headers=request_headers,
        json=invalid_request_body_with_non_existent_staff
    )
    response = res.get_json()

    assert not response['success']
    assert response['message'] == 'cannot find specified staff'
    assert res.status_code == 404


def test_post_requests_fails_with_invalid_enum_value_in_body(
    invalid_request_body_with_invalid_enum_value, client, request_headers
):
    """
    Tests that response shows failure when request body has invalid enum value.

    Args:
        invalid_request_body_with_invalid_enum_value (dict): a request body
            with invalid enum value
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """
    res = client.post(
        requests_url(),
        headers=request_headers,
        json=invalid_request_body_with_invalid_enum_value
    )
    response = res.get_json()

    assert not response['success']
    assert (
        response['message']['product_area'][0] == 'Invalid enum value POLITICS'
    )
    assert res.status_code == 400


def test_post_requests_fails_with_invalid_priority_in_body(
    invalid_request_body_with_invalid_priority, client, request_headers
):
    """
    Tests that response shows failure when request body has invalid enum value.

    Args:
        invalid_request_body_with_invalid_enum_value (dict): a request body
            with invalid enum value
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """
    res = client.post(
        requests_url(),
        headers=request_headers,
        json=invalid_request_body_with_invalid_priority
    )
    response = res.get_json()

    assert not response['success']
    assert (
        response['message'] == 'priority value must be between 0 and 100'
    )
    assert res.status_code == 400


def test_post_requests_fails_with_bad_json_in_body(
    bad_request_json_string, client, request_headers
):
    """
    Tests that response shows failure when request body has ill-formed json
    string.

    Args:
        bad_request_json_string (dict): a request body with ill-formed json
            string
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """

    res = client.post(
        requests_url(), headers=request_headers, data=bad_request_json_string
    )
    response = res.get_json()

    assert not response['success']
    assert res.status_code == 400


def test_post_requests_fails_with_invalid_string_length_in_body(
    invalid_request_body_with_invalid_string_length, client, request_headers
):
    """
    Tests that response shows failure when request body has invalid
    string length in body.

    Args:
        invalid_request_body_with_invalid_string_length (dict): a request body
            with invalid string length
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """
    res = client.post(
        requests_url(),
        headers=request_headers,
        json=invalid_request_body_with_invalid_string_length
    )
    response = res.get_json()

    assert not response['success']
    assert response['message'] == {
        'description': ['string cannot be longer than 250']
    }
    assert res.status_code == 400


def test_post_requests_fails_with_invalid_invalid_target_date_in_body(
    invalid_request_body_with_invalid_date, client, request_headers
):
    """
    Tests that response shows failure when request body has invalid
    target date.

    Args:
        invalid_request_body_with_invalid_string_length (dict): a request body
            with invalid string length
        client (FlaskClient): a test client created by a fixture.
        request_headers (dict): a header created by a fixture.
    """
    res = client.post(
        requests_url(),
        headers=request_headers,
        json=invalid_request_body_with_invalid_date
    )
    response = res.get_json()

    assert not response['success']
    assert response['message'] == {
        'target_date': ['date can only be a later time in the future']
    }
    assert res.status_code == 400
