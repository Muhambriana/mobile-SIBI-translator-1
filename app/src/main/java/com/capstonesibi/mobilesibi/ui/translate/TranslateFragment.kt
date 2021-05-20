package com.capstonesibi.mobilesibi.ui.translate

import android.os.Bundle
import androidx.fragment.app.Fragment
import com.capstonesibi.mobilesibi.R
import android.Manifest
import android.app.Activity
import android.content.Intent
import android.content.pm.PackageManager
import android.os.Environment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import androidx.lifecycle.ViewModelProvider
import com.capstonesibi.mobilesibi.databinding.FragmentTranslateBinding
import io.fotoapparat.Fotoapparat
import io.fotoapparat.configuration.CameraConfiguration
import io.fotoapparat.log.logcat
import io.fotoapparat.log.loggers
import io.fotoapparat.parameter.ScaleType
import io.fotoapparat.selector.*
import io.fotoapparat.view.CameraView
import java.io.File


class TranslateFragment : Fragment() {
    private var fotoapparat: Fotoapparat? = null
    private val example = "Result.png"
    private val externalStorage: String = Environment.getExternalStorageState()
    private val dest = File(externalStorage, example)
    private var fotoApparatState : FotoApparatState? = null
    private var cameraStatus : CameraState? = null
    private var flashState: FlashState? = null
    private lateinit var fragmentTransleteBinding: FragmentTranslateBinding

    private val permissions = arrayOf(Manifest.permission.CAMERA, Manifest.permission.WRITE_EXTERNAL_STORAGE, Manifest.permission.READ_EXTERNAL_STORAGE)

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        fragmentTransleteBinding = FragmentTranslateBinding.inflate(layoutInflater)
        return fragmentTransleteBinding.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        if (activity != null) {

            createFotoapparat()

            cameraStatus = CameraState.BACK
            flashState = FlashState.OFF
            fotoApparatState = FotoApparatState.OFF

            fragmentTransleteBinding.fabStart.setOnClickListener {
                takePhoto()
            }

            fragmentTransleteBinding.fabSwitchCamera.setOnClickListener {
                switchCamera()
            }

            fragmentTransleteBinding.fabFlash.setOnClickListener {
                changeFlashState()
            }
        }


    }

    private fun createFotoapparat(){
        val cameraView = fragmentTransleteBinding.cameraView

        fotoapparat = context?.let {
            Fotoapparat(
                context = it,
                view = cameraView,
                scaleType = ScaleType.CenterCrop,
                lensPosition = back(),
                logger = loggers(
                    logcat()
                ),
                cameraErrorCallback = { error ->
                    println("Recorder errors: $error")
                }
            )
        }
    }

    private fun changeFlashState() {
        fotoapparat?.updateConfiguration(
            CameraConfiguration(
                flashMode = if(flashState == FlashState.TORCH) off() else torch()
            )
        )

        flashState = if(flashState == FlashState.TORCH) FlashState.OFF
        else FlashState.TORCH
    }

    private fun switchCamera() {
        fotoapparat?.switchTo(
            lensPosition =  if (cameraStatus == CameraState.BACK) front() else back(),
            cameraConfiguration = CameraConfiguration()
        )

        cameraStatus = if(cameraStatus == CameraState.BACK) CameraState.FRONT
        else CameraState.BACK
    }

    private fun takePhoto() {
        if (hasNoPermissions()) {
            requestPermission()
        }else{
            fotoapparat
                ?.takePicture()
                ?.saveToFile(dest)
        }
    }

    override fun onStart() {
        super.onStart()
        if (hasNoPermissions()) {
            requestPermission()
        }else{
            fotoapparat?.start()
            fotoApparatState = FotoApparatState.ON
        }
    }

    private fun hasNoPermissions(): Boolean{
        return context?.let {
            ContextCompat.checkSelfPermission(
                it,
                Manifest.permission.READ_EXTERNAL_STORAGE)
        } != PackageManager.PERMISSION_GRANTED || ContextCompat.checkSelfPermission(
            context!!,
            Manifest.permission.WRITE_EXTERNAL_STORAGE) != PackageManager.PERMISSION_GRANTED || ContextCompat.checkSelfPermission(
            context!!,
            Manifest.permission.CAMERA) != PackageManager.PERMISSION_GRANTED
    }

    private fun requestPermission(){
        ActivityCompat.requestPermissions(context as Activity, permissions,0)
    }

    override fun onStop() {
        super.onStop()
        fotoapparat?.stop()
        FotoApparatState.OFF
    }

    override fun onResume() {
        super.onResume()
        if(!hasNoPermissions() && fotoApparatState == FotoApparatState.OFF){
            val intent = Intent(context, FragmentTranslateBinding::class.java)
            startActivity(intent)
            activity?.finish()
        }
    }

}

enum class CameraState{
    FRONT, BACK
}

enum class FlashState{
    TORCH, OFF
}

enum class FotoApparatState{
    ON, OFF
}
