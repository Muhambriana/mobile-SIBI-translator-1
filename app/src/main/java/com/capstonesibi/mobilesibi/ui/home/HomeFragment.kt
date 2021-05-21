package com.capstonesibi.mobilesibi.ui.home

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.DividerItemDecoration
import androidx.recyclerview.widget.GridLayoutManager
import androidx.recyclerview.widget.LinearLayoutManager
import com.capstonesibi.mobilesibi.data.Sibi
import com.capstonesibi.mobilesibi.databinding.FragmentHomeBinding
import com.capstonesibi.mobilesibi.ui.adapter.SibiAdapter
import com.capstonesibi.mobilesibi.utils.SibiData

class HomeFragment : Fragment() {
    private var _binding: FragmentHomeBinding? = null
    private val binding get() = _binding
    private var list: ArrayList<Sibi> = arrayListOf()
    private lateinit var sibiAdapter: SibiAdapter
    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        _binding =
            FragmentHomeBinding.inflate(LayoutInflater.from(inflater.context), container, false)
        return binding?.root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        list.addAll(SibiData.listData)
        sibiAdapter = SibiAdapter(list)
        setUpRecyclerView()
    }

    private fun setUpRecyclerView() {
        binding?.rvSibi?.apply {
            layoutManager = GridLayoutManager(context,2)
            adapter = sibiAdapter
            setHasFixedSize(true)
            addItemDecoration(DividerItemDecoration(context, LinearLayoutManager.VERTICAL))
        }
    }

    override fun onDestroy() {
        super.onDestroy()
        _binding = null
    }

}