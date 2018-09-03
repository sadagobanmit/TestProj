node('master') {
    // We have to checkout to a workspace with a shorted path to get around windows path name restrictions.
    // This also has a side benefit of ensuring that the worker will only use the amount of disk space
    // needed for a single build. The downside is that we can never run concurrent builds on this worker
    // and the workspaces are lost after the next build runs
    ws("C:\\wsws") {

        try {
            stage ("Clean Workspace") {
                deleteDir()
            }

            stage ("Build") {
                withEnv(
                    [
                        "PATH=${env.PATH};C:\\Program Files\\Git\\usr\\bin;C:\\Program Files\\CMake\\bin",                        
                        "JOB_NAME=10.1 Test Project"
                    ]
                ) {
                    dir('E:\\WSNTSrc\\Releases\\TestProj\\TestProj\\HelloWorld') {
					
						//bat 'mkdir build'
						//bat 'cd build'
						bat 'cmake .. -G "Visual Studio 12 2013 Win64'
						bat 'cmake --build .'
						//bat 'cmake .. -G "Visual Studio 12 2013 Win64" -DCMAKE_PREFIX_PATH=C:/Qt/5.9.1/msvc2017_64'
						//bat "\"${tool 'MSBuild'}\" HelloWorld.sln /p:Configuration=Release /p:Platform=\"x64\" /p:ProductVersion=1.0 /m"
                    }
                }
            }

            
            
        } catch (e) {
            currentBuild.result = "FAILED"
            throw e
        }
    }
}


