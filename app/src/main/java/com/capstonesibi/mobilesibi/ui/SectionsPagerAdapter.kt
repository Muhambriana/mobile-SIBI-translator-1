package com.capstonesibi.mobilesibi.ui

import android.content.Context
import androidx.annotation.StringRes
import androidx.fragment.app.Fragment
import androidx.fragment.app.FragmentManager
import androidx.fragment.app.FragmentPagerAdapter
import com.capstonesibi.mobilesibi.R
import com.capstonesibi.mobilesibi.ui.home.HomeFragment
import com.capstonesibi.mobilesibi.ui.translate.TranslateFragment

class SectionsPagerAdapter(private val mContext: Context, fm: FragmentManager) : FragmentPagerAdapter(fm, BEHAVIOR_RESUME_ONLY_CURRENT_FRAGMENT) {

    companion object {
        @StringRes
        private val TAB_TITLES = intArrayOf(R.string.fragment_home, R.string.fragment_translate)
    }

    override fun getItem(position: Int): Fragment =
        when (position) {
            0 -> HomeFragment()
            1 -> TranslateFragment()
            else -> Fragment()
        }

    override fun getPageTitle(position: Int): CharSequence? = mContext.resources.getString(TAB_TITLES[position])

    override fun getCount(): Int = 2

}