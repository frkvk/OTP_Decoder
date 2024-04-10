# OTP_Decoder
# Why OTP_Decoder
I want to export Google Authenticator QR Codes to flipper zero, and it doesnt have camera, so i need the algoritm and the secret key
In my case i use this app for Flipper zero: https://github.com/akopachov/flipper-zero_authenticator/wiki/How-to-add-new-token%3F
If your codes doesnt work, change the offsett.

Compiling your .proto file:
    Download Protocol Buffers Compiler for Windows:
        Visit the Protocol Buffers GitHub release page: https://github.com/protocolbuffers/protobuf/releases
        Find the latest stable version for Windows and download the corresponding zip file, like protoc-3.x.x-win64.zip.

    Extract the Zip File:
        Extract the downloaded zip file to a location of your choice. For example, you can create a folder called "protobuf" in your C:\ directory and extract the files there.

    Add Compiler Path to PATH Environment Variable:
        Right-click on "This PC" or "My Computer" and select "Properties."
        Click on "Advanced system settings" on the left panel.
        Click on "Environment Variables."
        In the "System Variables" section, find the PATH variable and click "Edit."
        Add the path to the directory containing protoc.exe at the end of the list, separated by a semicolon (;). For example, if you extracted protoc to C:\protobuf, add C:\protobuf to the path.
        Click "OK" to close the windows and save the changes.

    Verify the Installation:
        Open a new Command Prompt (cmd) window and type protoc --version. You should see the version of Protocol Buffers compiler you installed.

Once you have installed protoc, you can use the command protoc --python_out=. migration.proto in the directory containing your migration.proto file to compile it and generate the corresponding Python files (migration_pb2.py and migration_pb2_grpc.py). Then, you can import and use the generated classes in your Python script.

Navigate to your project folder using the command line.
Then execute the following command:

css

protoc --python_out=. --proto_path="Project folder path" migration.proto

Replace "qr_code_data_url" with your export variable. It is advisable not to export more than 3 QR codes from Google Authenticator at once.
You will receive the data in the console.

# Credits to https://gist.github.com/mapster/4b8b9f8f6b92cc1ca58ae5506e0508f7
