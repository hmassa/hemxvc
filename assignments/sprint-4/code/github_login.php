<?php

    session_start();
    include 'hybridauth-3.3.0/src/autoload.php';

    $config = [
        'callback' => 'http://ec2-3-134-97-105.us-east-2.compute.amazonaws.com/home.php', // Hybridauth\HttpClient\Util::getCurrentUrl() or http://ec2-3-134-97-105.us-east-2.compute.amazonaws.com/hybridauth-3.3.0/examples/example_01.php

        'keys' => [ 'id' => '***', 'secret' => '***' ], // Your Github application credentials

        /* optional : set scope
            'scope' => 'user:email', */

        /* optional : set debug mode
            'debug_mode' => true,
            // Path to file writeable by the web server. Required if 'debug_mode' is not false
            'debug_file' => __FILE__ . '.log', */

        /* optional : customize Curl settings
            // for more information on curl, refer to: http://www.php.net/manual/fr/function.curl-setopt.php  
            'curl_options' => [
                // setting custom certificates
                CURLOPT_SSL_VERIFYPEER => true,
                CURLOPT_CAINFO         => '/path/to/your/certificate.crt',
                // set a valid proxy ip address
                CURLOPT_PROXY => '*.*.*.*:*',
                // set a custom user agent
                CURLOPT_USERAGENT      => ''
            ] */
    ];

    $github = new Hybridauth\Provider\GitHub($config);
    $github->authenticate();

//    try {
//        $userProfile = $github->getUserProfile();
//        echo 'Hi '.$userProfile->displayName;
//    }
//    catch (Hybridauth\Exception\HttpClientFailureException $e) {
//        echo 'Curl text error message : '.$github->getHttpClient()->getResponseClientError();
//    }
//    catch (Hybridauth\Exception\HttpRequestFailedException $e) {
//        echo 'Raw API Response: '.$github->getHttpClient()->getResponseBody();
//    }
//    catch (\Exception $e) {
//        echo 'Oops! We ran into an unknown issue: '.$e->getMessage();
//    }

    $github->disconnect();

?>
