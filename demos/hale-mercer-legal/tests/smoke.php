<?php
use Illuminate\Contracts\Http\Kernel;
use Illuminate\Http\Request;

require __DIR__.'/../vendor/autoload.php';
$app = require __DIR__.'/../bootstrap/app.php';
$kernel = $app->make(Kernel::class);

$paths = ['/', '/practice-areas', '/attorneys', '/insights', '/consultation'];
foreach ($paths as $path) {
    $response = $kernel->handle(Request::create($path, 'GET'));
    if ($response->getStatusCode() !== 200) {
        fwrite(STDERR, "Smoke failure {$path}: {$response->getStatusCode()}\n");
        exit(1);
    }
    $kernel->terminate(Request::create($path, 'GET'), $response);
}
echo "Laravel smoke passed: ".count($paths)." routes\n";
